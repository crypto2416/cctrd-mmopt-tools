# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: algo_params.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x61lgo_params.proto\x12\x0estrategy_proto\x1a\x0c\x63ommon.proto\"\xa1\x02\n\x0b\x41LGO_PARAMS\x12\x13\n\x0bsymbol_base\x18\x01 \x01(\t\x12\x0c\n\x04\x61lgo\x18\x02 \x01(\t\x12\x10\n\x08\x64uration\x18\x03 \x01(\t\x12\x12\n\norder_size\x18\x04 \x01(\t\x12\x14\n\x0cmin_qty_algo\x18\x05 \x01(\x01\x12\x12\n\nstart_time\x18\x06 \x01(\t\x12\x10\n\x08\x65nd_time\x18\x07 \x01(\t\x12\x13\n\x0blimit_price\x18\x08 \x01(\x01\x12\x19\n\x11take_profit_price\x18\t \x01(\x01\x12\x13\n\x0b\x64isplay_qty\x18\n \x01(\x01\x12\x0c\n\x04mode\x18\x0b \x01(\x05\x12\x11\n\trandomise\x18\x0c \x01(\x08\x12\x11\n\tpeg_shift\x18\r \x01(\x01\x12\x14\n\x0c\x62ps_to_cross\x18\x0e \x01(\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'algo_params_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ALGO_PARAMS._serialized_start=52
  _ALGO_PARAMS._serialized_end=341
# @@protoc_insertion_point(module_scope)
