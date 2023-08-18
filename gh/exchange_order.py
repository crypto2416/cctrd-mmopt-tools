#!/usr/bin/python

import ctypes

import pb_msg_pb2
import pb_common_pb2
import os
import uuid

import time
from datetime import datetime  

class ExchangeOrder:

  def __init__(self, new_order_msg, identity=''):
    self.msg = new_order_msg
    self.identity = identity if identity else self.msg.src
    self.ordid = str(uuid.uuid4().int & (1<<64)-1).encode()
    self.status = new_order_msg.order.status
    self.filled_prx = 0
    self.filled_qty = 0
    self.qty = self.msg.order.order_qty
    self.prx = self.msg.order.order_prx
    self.side = self.msg.order.buysell
    self.trades = {}
    
  def order_status(self, status, filled_qty = 0, filled_prx = 0, **kwargs):
    if status == 'Filled' and self.filled_qty + filled_qty < self.qty:
      status = 'PartialFilled'
      
    self.status = pb_msg_pb2.PB_OrderStatusEnum.Value('OrderStatus_'+status) 
    msg = self.msg
    apimsg = pb_msg_pb2.PB_Msg()
    apimsg.type = pb_msg_pb2.PB_Msg_DataTypeEnum.TRDMSG
    # set up order info
    fmsg = apimsg.fmsg
    fmsg.src = self.identity
    fmsg.dst = b"ExchForward"
    fmsg.sty = msg.sty
    fmsg.type = pb_msg_pb2.PB_F_DataTypeEnum.Value('FOrdSt')
    
    # set up order info
    fmsg.ordst.sym = msg.order.sym
    fmsg.ordst.sym_exch = msg.order.sym_exch
    fmsg.ordst.ordid_client = msg.order.ordid_client
  
    fmsg.ordst.buysell = self.side
    fmsg.ordst.order_qty = self.qty
    fmsg.ordst.order_prx = self.prx

    fmsg.ordst.status = self.status

    if self.filled_qty + filled_qty > 0 :
      self.filled_prx = (self.filled_qty * self.filled_prx + filled_prx*filled_qty) / (self.filled_qty + filled_qty)
      self.filled_qty += filled_qty
  
      fmsg.ordst.filled_prx = self.filled_prx
      fmsg.ordst.filled_qty = self.filled_qty
    
    # 2022-08-04T07:25:33Z
    fmsg.ordst.timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    fmsg.ordst.timestamp_ms = int(datetime.now().timestamp() * 1000)
    ordid_internal = self.ordid
    fmsg.ordst.ordid_internal = ordid_internal

    for key, value in kwargs.items():
      if isinstance(value, str):
        exec('fmsg.ordst.{}="{}"'.format(key, value))
      else:
        exec('fmsg.ordst.{}={}'.format(key, value))
    return apimsg
  
  def order_trade(self, filled_qty, filled_prx = 0):
    msg = self.msg
    apimsg = pb_msg_pb2.PB_Msg()
    apimsg.type = pb_msg_pb2.PB_Msg_DataTypeEnum.TRDMSG
    # set up order info
    fmsg = apimsg.fmsg
    fmsg.src = self.identity
    fmsg.dst = b"ExchForward"
    fmsg.sty = msg.sty
    fmsg.type = pb_msg_pb2.PB_F_DataTypeEnum.Value('FTrade')
    
    # set up order info
    fmsg.trade.sym = msg.order.sym
    fmsg.trade.sym_exch = msg.order.sym_exch
    fmsg.trade.ordid_client = msg.order.ordid_client
    fmsg.trade.account = msg.order.account
    fmsg.trade.book = msg.order.book
    fmsg.trade.exchange = b'ExchSim'
  
    fmsg.trade.trade_prx = filled_prx if filled_prx else msg.order.order_prx 
    fmsg.trade.trade_qty = filled_qty
  
    # 2022-08-04T07:25:33Z
    fmsg.trade.timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    fmsg.trade.timestamp_ms = int(datetime.now().timestamp() * 1000)
  
    ordid_internal = self.ordid
    fmsg.trade.ordid_internal = ordid_internal
    fmsg.trade.trdid_exchange = str(uuid.uuid4().int & (1<<64)-1).encode()
    fmsg.trade.ordid_parent = msg.order.ordid_parent
    self.trades[fmsg.trade.trdid_exchange] = apimsg

    return apimsg

class ShadowOrder(ExchangeOrder):
  def __init__(self, new_order_msg, identity=''):
    super().__init__(new_order_msg, identity)
    self.real_orders = {} # id : ExchangeOrder
    self.trades = {}

  def order_invite(self, qty):
    apimsg = pb_msg_pb2.PB_Msg()
    apimsg.type = pb_msg_pb2.PB_Msg_DataTypeEnum.TRDMSG
    fmsg = apimsg.fmsg
    fmsg.type = pb_msg_pb2.PB_F_DataTypeEnum.Value('FIMEI')
    ime_invite = fmsg.ime_invite.value.add() 
    ime_invite.ordid_internal = self.ordid
    ime_invite.ordid_client = self.msg.order.ordid_client
    ime_invite.quantity = self.qty
    ime_invite.timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    ime_invite.timestamp_ms = int(datetime.now().timestamp() * 1000)
    return apimsg
    
  def create_real_order(self, msg_):
    assert(msg_.order.ordid_parent == self.ordid.decode('utf-8'))
    real_order = ExchangeOrder(msg_, self.identity)
    self.real_orders[msg_.order.ordid_client] = real_order
    return real_order
  

