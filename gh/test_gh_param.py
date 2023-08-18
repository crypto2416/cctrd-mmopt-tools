#!/usr/bin/python
import time
import zmq
import threading
import ctypes
import pb_msg_pb2
import pb_common_pb2
import option_hedging_pb2
import os
import uuid
from datetime import datetime
from tabulate import tabulate

class ZmqSubThread(threading.Thread):
  def __init__(self, func, serverIP, port):
    threading.Thread.__init__(self)
    self.context = zmq.Context()
    self.socket = self.context.socket(zmq.SUB)
    self.serverIP = serverIP
    self.port = port
    self.func = func
    self.update_time = datetime.now()
    
    # self.socket.setsockopt_string(zmq.IDENTITY, identity) # utf--8
    self.socket.connect('tcp://{0}:{1}.'.format(serverIP, port))
    self.socket.setsockopt(zmq.SUBSCRIBE, b'')


    self.parameters_book = {}

  def run(self):
    self.func(self)

def print_param_table(parameters_book):
  # headers = ['key', 'sym', 'mode', 'book', 'greek_recalculation_timeout', 'greek_pool_delta_min', 'greek_pool_delta_max', 'hedge_delta_symbols', 'greek_pool_symbols', 'tenor_delta_risk','tenor_gamma_risk', 'tenor_vega_risk', 'total_delta_risk', 'total_gamma_risk', 'total_vega_risk']
  # headers = ['symbol', 'mode', 'book', 'hedge_delta_symbols', 'greek_pool_symbols', 'tenor_delta_risk','tenor_gamma_risk', 'tenor_vega_risk', 'total_delta_risk', 'total_gamma_risk', 'total_vega_risk', 'hedging_position_risk']
  headers = ['symbol', 'mode', 'book', 'hedge_delta_symbols', 'greek_pool_symbols', 'delta_to_hedge','gamma_to_hedge', 'vega_to_hedge', 'delta_to_hedge', 'hedging_position', 'position_to_hedge']
  keys = parameters_book.keys();
  table = []
  for key, p in parameters_book.items():
    row = []
    for i in headers:
      row.append(getattr(p[i], 'value_str').replace(",", "\n"))
    if getattr(p['sym_type'], 'value_str') == '1':
      table.append(row)
      syms = getattr(p['greek_pool_symbols'], 'value_str').strip(' ,').split(",")
      for s in syms:
        if s:
          psym = parameters_book[s]
          row = []
          for j in headers:
            row.append(getattr(psym[j], 'value_str').replace(",", "\n"))
          table.append(row)


#  for key, p in parameters_book.items():
#    if p.sym_type == 1: # SymbolType_OPTION_PORTFOLIO
#      table.append([p.key, sym, p.attr.book, p.greek_recalculation_timeout, p.greek_pool_delta_min + "," + "greek_pool_delta_max", '\n'.join(p.greek_pool_symbols), \
#          p.tenor_delta_risk, p.tenor_gamma_risk, p.tenor_vega_risk, \
#          p.total_delta_risk, p.total_gamma_risk, p.total_vega_risk])
  os.system('clear')
  # widths = [8 for i in range(len(headers))]
  widths = [None] * len(headers)
  # widths = [8,4,4,8,8,3,6,3,3,3,3,3]
  # print(len(widths), len(headers))
  print(tabulate(table, headers, tablefmt="psql")) # , maxcolwidths=widths))

def loopsub(server):
  timestamp_ms = 0
  socket = server.socket
  while True:
    if not socket.closed:
      message = socket.recv()
      recv = pb_msg_pb2.PB_Msg()
      recv.ParseFromString(message)
      if recv.type == pb_msg_pb2.PB_Msg_DataTypeEnum.Value('STYMSG') and recv.cmd.type == pb_msg_pb2.PB_S_DataTypeEnum.Value('STYMCMD'):
        # print(recv)
        data = recv.cmd
        # server.parameters_book[data.src] = data.mcmd.para
        server.parameters_book[getattr(data.mcmd.para['symbol'], 'value_str')] = data.mcmd.para
        if (datetime.now() - server.update_time).total_seconds() > 1: 
          print_param_table(server.parameters_book)
          server.update_time = datetime.now()
    else:
      print("socket2 is closed, cannot receive any message...")
      break

def main():
  zmqThread3 = ZmqSubThread(loopsub, '127.0.0.1', '35567')
  zmqThread3.start()
  
  while(True):
    pass;
        
if __name__ == '__main__':
  main()

