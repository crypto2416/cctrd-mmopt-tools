# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pb_msg.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import pb_common_pb2 as pb__common__pb2
import pb_firm_msg_pb2 as pb__firm__msg__pb2
try:
  pb__common__pb2 = pb__firm__msg__pb2.pb__common__pb2
except AttributeError:
  pb__common__pb2 = pb__firm__msg__pb2.pb_common_pb2
try:
  pb__mkt__msg__pb2 = pb__firm__msg__pb2.pb__mkt__msg__pb2
except AttributeError:
  pb__mkt__msg__pb2 = pb__firm__msg__pb2.pb_mkt_msg_pb2
try:
  pb__common__pb2 = pb__firm__msg__pb2.pb__common__pb2
except AttributeError:
  pb__common__pb2 = pb__firm__msg__pb2.pb_common_pb2
import pb_mkt_msg_pb2 as pb__mkt__msg__pb2
try:
  pb__common__pb2 = pb__mkt__msg__pb2.pb__common__pb2
except AttributeError:
  pb__common__pb2 = pb__mkt__msg__pb2.pb_common_pb2
import pb_sty_msg_pb2 as pb__sty__msg__pb2
try:
  pb__common__pb2 = pb__sty__msg__pb2.pb__common__pb2
except AttributeError:
  pb__common__pb2 = pb__sty__msg__pb2.pb_common_pb2
import pb_hbt_msg_pb2 as pb__hbt__msg__pb2
try:
  pb__common__pb2 = pb__hbt__msg__pb2.pb__common__pb2
except AttributeError:
  pb__common__pb2 = pb__hbt__msg__pb2.pb_common_pb2
import pb_act_msg_pb2 as pb__act__msg__pb2
try:
  pb__common__pb2 = pb__act__msg__pb2.pb__common__pb2
except AttributeError:
  pb__common__pb2 = pb__act__msg__pb2.pb_common_pb2

from pb_common_pb2 import *
from pb_firm_msg_pb2 import *
from pb_mkt_msg_pb2 import *
from pb_sty_msg_pb2 import *
from pb_hbt_msg_pb2 import *
from pb_act_msg_pb2 import *

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cpb_msg.proto\x12\x04omgw\x1a\x0fpb_common.proto\x1a\x11pb_firm_msg.proto\x1a\x10pb_mkt_msg.proto\x1a\x10pb_sty_msg.proto\x1a\x10pb_hbt_msg.proto\x1a\x10pb_act_msg.proto\"\xc6\x01\n\x06PB_Msg\x12\'\n\x04type\x18\x01 \x01(\x0e\x32\x19.omgw.PB_Msg_DataTypeEnum\x12\x1b\n\x03\x63md\x18\x02 \x01(\x0b\x32\x0e.omgw.PB_S_Msg\x12\x1c\n\x04mmsg\x18\x03 \x01(\x0b\x32\x0e.omgw.PB_M_Msg\x12\x1c\n\x04\x66msg\x18\x04 \x01(\x0b\x32\x0e.omgw.PB_F_Msg\x12\x1c\n\x04hmsg\x18\x05 \x01(\x0b\x32\x0e.omgw.PB_H_Msg\x12\x1c\n\x04\x61msg\x18\x06 \x01(\x0b\x32\x0e.omgw.PB_A_Msg*Q\n\x13PB_Msg_DataTypeEnum\x12\n\n\x06STYMSG\x10\x00\x12\n\n\x06MKTMSG\x10\x01\x12\n\n\x06TRDMSG\x10\x02\x12\n\n\x06HBTMSG\x10\x03\x12\n\n\x06\x41\x43TMSG\x10\x04\x42\x03\xf8\x01\x01P\x00P\x01P\x02P\x03P\x04P\x05\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pb_msg_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\370\001\001'
  _PB_MSG_DATATYPEENUM._serialized_start=331
  _PB_MSG_DATATYPEENUM._serialized_end=412
  _PB_MSG._serialized_start=131
  _PB_MSG._serialized_end=329
# @@protoc_insertion_point(module_scope)