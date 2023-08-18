#!/usr/bin/python
import time
import zmq
import threading
import ctypes
import pb_msg_pb2
import pb_common_pb2
import os
import uuid
from tabulate import tabulate
from datetime import datetime
from exchange_order import ExchangeOrder

import argparse
import random

args = {}

count = 1;

def print_order_table(order_book):
  headers = ['orderid', 'sym', 'status', 'qty', 'price', 'side', 'trades']
  table = []
  for i, exch_order in order_book.items():
    trades = []
    s = exch_order.msg.order
    for t in exch_order.trades.values(): 
        trades.append(str(t.fmsg.trade.trade_qty)+'@'+str(t.fmsg.trade.trade_prx))
    # if exch_order.status != pb_msg_pb2.PB_OrderStatusEnum.OrderStatus_Cancelled:
    table.append([i, s.sym, pb_msg_pb2.PB_OrderStatusEnum.Name(exch_order.status), s.order_qty, s.order_prx, pb_msg_pb2.PB_OrderBuySellEnum.Name(s.buysell), '\n'.join(map(str, trades))])

  os.system('clear')
  print(tabulate(table, headers, tablefmt="psql"))
  print('ack the order with examples:')
  print('send_order_status("00000000id", "Live")')
  print('send_order_trade("00000000id", 20000, 10)')

class ZmqClientThread(threading.Thread):
  def __init__(self, func, serverIP, port, identity):
    threading.Thread.__init__(self)
    self.context = zmq.Context()
    self.socket = self.context.socket(zmq.DEALER)
    self.serverIP = serverIP
    self.identity = identity
    self.port = port
    self.func = func
    
    # connection set up
    self.socket.setsockopt_string(zmq.IDENTITY, identity) # utf--8
    self.socket.connect('tcp://{0}:{1}.'.format(serverIP, port))

  def send_msg(self, data):
    if not self.socket.closed:
      self.socket.send(data)
    else:
      print('scoket is closed, cant send messages ... ')

  def run(self):
    self.func(self.socket)


class ZmqServerThread(threading.Thread):
  def __init__(self, func, port):
    threading.Thread.__init__(self)
    self.context = zmq.Context()
    self.socket = self.context.socket(zmq.ROUTER)
    self.socket.bind("tcp://*:{}".format(port))

    self.port = port
    self.func = func

    self.order_book = {} # id - status

  def send_order_status(self, oid, status, txt=''):
    if not self.socket.closed:
      if oid in self.order_book:
        exch_order = self.order_book[oid]  # TODO : list ?
        apimsg = exch_order.order_status(status, comments=txt)
        self.send_msg(exch_order.identity, apimsg.SerializeToString())
        # print(apimsg)
        print_order_table(self.order_book)
      else:
        print('{} is not in exch sim server. ignore the request'.format(oid))
    else:
      print("socket is closed, cannot receive any message...")
      exit(1)

  def send_order_trade(self, oid, filled_qty = 0, filled_prx = 0):
    print('send_order_trade'.format(oid))
    if not self.socket.closed:
      if oid in self.order_book:
        exch_order = self.order_book[oid]  # TODO : list ?
        if filled_qty == 0:
            filled_qty = exch_order.qty 
        if filled_prx == 0:
            filled_prx = exch_order.prx
        apimsg_ordst = exch_order.order_status("Filled", filled_qty, filled_prx)
        self.send_msg(exch_order.identity, apimsg_ordst.SerializeToString())
        print(apimsg_ordst)
        apimsg_trade = exch_order.order_trade(filled_qty, filled_prx)
        self.send_msg(exch_order.identity, apimsg_trade.SerializeToString())
        print(apimsg_trade)
        print_order_table(self.order_book)
      else:
        print('{} is not in exch sim server. ignore the request'.format(oid))
    else:
      print("socket is closed, cannot receive any message...")
      exit(1)

  def send_msg(self, identity, msg):
    if not self.socket.closed:
      self.socket.send_multipart([identity, msg])
    else:
      print("socket is closed, cannot receive any message...")
      exit(1)
 
  def run(self):
    self.func(self)

def loopserver(server):
  while True:
    if not server.socket.closed:
      identity, message = server.socket.recv_multipart()
      recv = pb_msg_pb2.PB_Msg()
      recv.ParseFromString(message)
      if recv.type != pb_msg_pb2.PB_Msg_DataTypeEnum.Value('TRDMSG'):
        continue # ignore heart beat for the demo
      fmsg = recv.fmsg
      assert(fmsg.type == pb_msg_pb2.PB_F_DataTypeEnum.Value('FOrder'))
      # if fmsg.order.ordid_client in order_book:
      #  order_book[fmsg.order.ordid_client].append(fmsg.order)
      # else:

      if fmsg.order.action == pb_msg_pb2.PB_OrderActionEnum.Value('OrderAction_New'):
        server.order_book[fmsg.order.ordid_client] = ExchangeOrder(fmsg)
        if args.reject_test:
            server.send_order_status(fmsg.order.ordid_client, "Error", "Rejected Test" + str(random.randint(0,0))) # auto new ack
        if args.auto_ack:
            server.send_order_status(fmsg.order.ordid_client, "Live") # auto new ack
        if args.auto_fill:
            global count
            if args.only_fill:
                if any(s in fmsg.order.sym for s in args.only_fill) or "FILL" in fmsg.order.strategy:
                    server.send_order_trade(fmsg.order.ordid_client)
            elif count < 30:
                count+=1
                server.send_order_trade(fmsg.order.ordid_client)
        elif args.housefill_test:
          exch_order = server.order_book[fmsg.order.ordid_client]
          if exch_order.qty > 0.008:
              server.send_order_trade(fmsg.order.ordid_client, filled_prx = exch_order.prx, filled_qty = exch_order.qty - 0.008)
        elif args.fullf_test:
          exch_order = server.order_book[fmsg.order.ordid_client]
          if exch_order.prx > 30000:
              server.send_order_trade(fmsg.order.ordid_client)
          elif exch_order.qty > 0.005:
              server.send_order_trade(fmsg.order.ordid_client, filled_prx = exch_order.prx, filled_qty = exch_order.qty - 0.005)

      elif fmsg.order.ordid_client in server.order_book:
        assert(fmsg.order.action == pb_msg_pb2.PB_OrderActionEnum.Value('OrderAction_Cancel'))
        exch_order = server.order_book[fmsg.order.ordid_client]
        assert(exch_order)
        if args.cancel:
            if args.only_cancel:
                if any(s in fmsg.order.sym for s in args.only_cancel) or "CANCEL" in fmsg.order.strategy:
                    server.send_order_status(fmsg.order.ordid_client, "Cancelled") # auto cancel ack
            else:
                server.send_order_status(fmsg.order.ordid_client, "Cancelled") # auto cancel ack
        else:
            server.send_order_status(fmsg.order.ordid_client, "Cancelling")

          # server.send_order_trade(fmsg.order.ordid_client) # auto cancel ack
      print_order_table(server.order_book)
    else:
      print("socket exchange is closed, cannot receive any message...")
      break

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--cancel', action='store_true', help='enable auto cancel')
  parser.add_argument('--auto_ack', action='store_true', help='enable auto ack.')
  parser.add_argument('--auto_fill', action='store_true', help='enable auto fill.')
  parser.add_argument('--housefill_test', action='store_true', help='test housefill.')
  parser.add_argument('--fullf_test', action='store_true', help='test 100% fully fill.')
  parser.add_argument('--reject_test', action='store_true', help='test reject.')
  parser.add_argument('--only_fill', type=str, action='append', help='only fill pattern in sym.')
  parser.add_argument('--only_cancel', type=str, action='append', help='only cancel pattern in sym.')
  parser.add_argument('--port', type=int, default=5556, help='only fill pattern in sym.')
  global args
  args = parser.parse_args()
  print(args)

  zmqThreadExch = ZmqServerThread(loopserver, args.port)
  zmqThreadExch.start()

  while(True):
    print('ack the order with examples:')
    print('send_order_status("00000000id", "Live")')
    print('send_order_trade("00000000id", 20000, 10)')
    print('q is quit')
    data = input()
    if data == 'q':
      os._exit(1)
    else:
      try :
        msg = eval('zmqThreadExch.'+data)
      except Exception as e:
        print('wrong input of: '+data)
        print(e)
        continue
        
if __name__ == '__main__':
  main()

