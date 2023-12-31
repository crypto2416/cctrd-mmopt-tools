# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: algo_order.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x61lgo_order.proto\x12\x0estrategy_proto\x1a\x0c\x63ommon.proto\"\xf1\x1a\n\tAlgoOrder\x12\x0b\n\x03sym\x18\t \x01(\t\x12,\n\x04\x61ttr\x18\n \x01(\x0b\x32\x1e.strategy_proto.OrderAttribute\x12\x16\n\x0eorderid_client\x18\x14 \x01(\t\x12\x18\n\x10orderid_internal\x18\x15 \x01(\t\x12\x37\n\norder_side\x18\x16 \x01(\x0e\x32#.strategy_proto.AlgoOrder.OrderSide\x12;\n\x0corder_status\x18\x17 \x01(\x0e\x32%.strategy_proto.AlgoOrder.OrderStatus\x12\x13\n\x0border_price\x18\x18 \x01(\x01\x12\x16\n\x0eorder_quantity\x18\x19 \x01(\x01\x12\x16\n\x0eorder_notional\x18\x1a \x01(\x01\x12\x14\n\x0c\x66illed_price\x18\x1b \x01(\x01\x12\x17\n\x0f\x66illed_quantity\x18\x1c \x01(\x01\x12\x17\n\x0f\x66illed_notional\x18\x1d \x01(\x01\x12\x43\n\x10price_constraint\x18) \x01(\x0b\x32).strategy_proto.AlgoOrder.PriceConstraint\x12\x41\n\x0ftime_constraint\x18* \x01(\x0b\x32(.strategy_proto.AlgoOrder.TimeConstraint\x12\x37\n\nsor_params\x18, \x01(\x0b\x32#.strategy_proto.AlgoOrder.SorParams\x12=\n\rcommon_params\x18- \x01(\x0b\x32&.strategy_proto.AlgoOrder.CommonParams\x12\x39\n\x0btwap_params\x18. \x01(\x0b\x32$.strategy_proto.AlgoOrder.TwapParams\x12?\n\x0eiceberg_params\x18/ \x01(\x0b\x32\'.strategy_proto.AlgoOrder.IcebergParams\x12=\n\rpegger_params\x18\x30 \x01(\x0b\x32&.strategy_proto.AlgoOrder.PeggerParams\x12=\n\rbasket_params\x18\x31 \x01(\x0b\x32&.strategy_proto.AlgoOrder.BasketParams\x12\x44\n\x11\x62\x61sket_leg_params\x18\x37 \x01(\x0b\x32).strategy_proto.AlgoOrder.BasketLegParams\x12,\n\tleg_order\x18\x38 \x03(\x0b\x32\x19.strategy_proto.AlgoOrder\x12\x1d\n\x15\x62\x61sket_orderid_client\x18\x39 \x01(\t\x12\x1f\n\x17\x62\x61sket_orderid_internal\x18: \x01(\t\x1a/\n\x0fPriceConstraint\x12\r\n\x05upper\x18\x01 \x01(\x01\x12\r\n\x05lower\x18\x02 \x01(\x01\x1a\xa8\x01\n\x0eTimeConstraint\x12\x10\n\x08interval\x18\x01 \x01(\x01\x12\x10\n\x08\x64uration\x18\x02 \x01(\x01\x12\x0e\n\x06repeat\x18\x03 \x01(\r\x12\x12\n\nstart_time\x18\x04 \x01(\t\x12\x10\n\x08\x65nd_time\x18\x05 \x01(\t\x12<\n\x08liq_pref\x18\x06 \x01(\x0e\x32*.strategy_proto.AlgoOrder.LiquidPreference\x1a\x95\x01\n\tSorParams\x12@\n\x0crouting_mode\x18\x01 \x01(\x0e\x32*.strategy_proto.AlgoOrder.OrderRoutingMode\x12\x18\n\x10target_depth_qty\x18\x02 \x01(\x01\x12\x16\n\x0esyms_n_weights\x18\x03 \x01(\t\x12\x14\n\x0climit_repeat\x18\x04 \x01(\x08\x1a<\n\nTwapParams\x12\x13\n\x0blimit_price\x18\x01 \x01(\x01\x12\x19\n\x11take_profit_price\x18\x02 \x01(\x01\x1a\x9a\x01\n\rIcebergParams\x12\x13\n\x0blimit_price\x18\x01 \x01(\x01\x12\x13\n\x0b\x64isplay_qty\x18\x02 \x01(\x01\x12\x11\n\trandomise\x18\x06 \x01(\x08\x12\x33\n\x04mode\x18\x07 \x01(\x0e\x32%.strategy_proto.AlgoOrder.IcebergMode\x12\x17\n\x0fstop_loss_price\x18\x08 \x01(\x01\x1a\x98\x01\n\x0cPeggerParams\x12\x13\n\x0blimit_price\x18\x01 \x01(\x01\x12\x19\n\x11take_profit_price\x18\x02 \x01(\x01\x12\x1a\n\x12\x63hild_tob_fraction\x18\x03 \x01(\x01\x12\x11\n\tpeg_shift\x18\x04 \x01(\x01\x12\x14\n\x0c\x62ps_to_cross\x18\x05 \x01(\x01\x12\x13\n\x0b\x64isplay_qty\x18\x06 \x01(\x01\x1a\xc0\x01\n\x0c\x43ommonParams\x12\x12\n\nstart_time\x18\x01 \x01(\t\x12\x10\n\x08\x65nd_time\x18\x02 \x01(\t\x12\x10\n\x08\x64uration\x18\x03 \x01(\x01\x12\x35\n\talgo_type\x18\x04 \x01(\x0e\x32\".strategy_proto.AlgoOrder.AlgoType\x12\x41\n\x0f\x64\x61rk_preference\x18\x05 \x01(\x0e\x32(.strategy_proto.AlgoOrder.DarkPreference\x1a\xc5\x01\n\x0c\x42\x61sketParams\x12\x35\n\talgo_type\x18\x01 \x01(\x0e\x32\".strategy_proto.AlgoOrder.AlgoType\x12\x19\n\x11\x65quation_constant\x18\x02 \x01(\x01\x12=\n\x11\x65quation_equality\x18\x03 \x01(\x0e\x32\".strategy_proto.AlgoOrder.Equality\x12\x10\n\x08num_legs\x18\x04 \x01(\x05\x12\x12\n\nleg_number\x18\x05 \x01(\x05\x1a\xd1\x01\n\x0f\x42\x61sketLegParams\x12\x37\n\nhedge_type\x18\x01 \x01(\x0e\x32#.strategy_proto.AlgoOrder.HedgeType\x12\x10\n\x08\x62\x61it_leg\x18\x02 \x01(\x08\x12\x11\n\thedge_leg\x18\x03 \x01(\x08\x12\x17\n\x0freference_price\x18\x0c \x01(\x01\x12\x13\n\x0b\x63oefficient\x18\r \x01(\x01\x12\x15\n\rmax_imbalance\x18\x11 \x01(\x01\x12\x1b\n\x13num_imbalance_tiers\x18\x12 \x01(\x05\"I\n\tOrderSide\x12\x15\n\x11OrderSide_UNKNOWN\x10\x00\x12\x11\n\rOrderSide_BUY\x10\x01\x12\x12\n\x0eOrderSide_SELL\x10\x02\"v\n\x0bOrderStatus\x12\x17\n\x13OrderStatus_CREATED\x10\x00\x12\x17\n\x13OrderStatus_PENDING\x10\x01\x12\x19\n\x15OrderStatus_ON_MARKET\x10\x02\x12\x1a\n\x16OrderStatus_OFF_MARKET\x10\x03\"\xfa\x01\n\x10LiquidPreference\x12\x19\n\x15LiquidPreference_TWAP\x10\x00\x12!\n\x1dLiquidPreference_TWAP_ENHANCE\x10\x01\x12 \n\x1cLiquidPreference_AGRESSIVE_0\x10\x02\x12 \n\x1cLiquidPreference_AGRESSIVE_1\x10\x03\x12 \n\x1cLiquidPreference_AGRESSIVE_2\x10\x04\x12 \n\x1cLiquidPreference_AGRESSIVE_3\x10\x05\x12 \n\x1cLiquidPreference_AGRESSIVE_4\x10\x06\"\xc4\x01\n\x10OrderRoutingMode\x12\x18\n\x14OrderRoutingMode_OFF\x10\x00\x12\x1c\n\x18OrderRoutingMode_DEFAULT\x10\x01\x12\x1f\n\x1bOrderRoutingMode_FILL_RATIO\x10\x02\x12\x1d\n\x19OrderRoutingMode_SLIPPAGE\x10\x03\x12\x1a\n\x16OrderRoutingMode_PRICE\x10\x04\x12\x1c\n\x18OrderRoutingMode_FAN_OUT\x10\x05\"\x86\x01\n\x08\x41lgoType\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04TWAP\x10\x01\x12\x0b\n\x07ICEBERG\x10\x02\x12\t\n\x05REFPX\x10\x03\x12\x0c\n\x08\x45QUATION\x10\x04\x12\t\n\x05HEDGE\x10\x05\x12\n\n\x06\x42\x41SKET\x10\x06\x12\x0f\n\x0bPASSTHROUGH\x10\x07\x12\x0c\n\x08\x44\x41RKPOOL\x10\x08\x12\n\n\x06PEGGER\x10\t\"5\n\x0bIcebergMode\x12\x0b\n\x07\x43LASSIC\x10\x00\x12\r\n\tWATERFALL\x10\x01\x12\n\n\x06SNIPER\x10\x02\"\x1d\n\tHedgeType\x12\x10\n\x0c\x43ROSS_SPREAD\x10\x00\"\x1c\n\x08\x45quality\x12\x07\n\x03GTE\x10\x00\x12\x07\n\x03LTE\x10\x01\"y\n\x0e\x44\x61rkPreference\x12\x1a\n\x16\x44\x61rkPreference_DEFAULT\x10\x00\x12\x1b\n\x17\x44\x61rkPreference_OPTIONAL\x10\x01\x12\x15\n\x11\x44\x61rkPreference_NO\x10\x02\x12\x17\n\x13\x44\x61rkPreference_ONLY\x10\x03\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'algo_order_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ALGOORDER._serialized_start=51
  _ALGOORDER._serialized_end=3492
  _ALGOORDER_PRICECONSTRAINT._serialized_start=1118
  _ALGOORDER_PRICECONSTRAINT._serialized_end=1165
  _ALGOORDER_TIMECONSTRAINT._serialized_start=1168
  _ALGOORDER_TIMECONSTRAINT._serialized_end=1336
  _ALGOORDER_SORPARAMS._serialized_start=1339
  _ALGOORDER_SORPARAMS._serialized_end=1488
  _ALGOORDER_TWAPPARAMS._serialized_start=1490
  _ALGOORDER_TWAPPARAMS._serialized_end=1550
  _ALGOORDER_ICEBERGPARAMS._serialized_start=1553
  _ALGOORDER_ICEBERGPARAMS._serialized_end=1707
  _ALGOORDER_PEGGERPARAMS._serialized_start=1710
  _ALGOORDER_PEGGERPARAMS._serialized_end=1862
  _ALGOORDER_COMMONPARAMS._serialized_start=1865
  _ALGOORDER_COMMONPARAMS._serialized_end=2057
  _ALGOORDER_BASKETPARAMS._serialized_start=2060
  _ALGOORDER_BASKETPARAMS._serialized_end=2257
  _ALGOORDER_BASKETLEGPARAMS._serialized_start=2260
  _ALGOORDER_BASKETLEGPARAMS._serialized_end=2469
  _ALGOORDER_ORDERSIDE._serialized_start=2471
  _ALGOORDER_ORDERSIDE._serialized_end=2544
  _ALGOORDER_ORDERSTATUS._serialized_start=2546
  _ALGOORDER_ORDERSTATUS._serialized_end=2664
  _ALGOORDER_LIQUIDPREFERENCE._serialized_start=2667
  _ALGOORDER_LIQUIDPREFERENCE._serialized_end=2917
  _ALGOORDER_ORDERROUTINGMODE._serialized_start=2920
  _ALGOORDER_ORDERROUTINGMODE._serialized_end=3116
  _ALGOORDER_ALGOTYPE._serialized_start=3119
  _ALGOORDER_ALGOTYPE._serialized_end=3253
  _ALGOORDER_ICEBERGMODE._serialized_start=3255
  _ALGOORDER_ICEBERGMODE._serialized_end=3308
  _ALGOORDER_HEDGETYPE._serialized_start=3310
  _ALGOORDER_HEDGETYPE._serialized_end=3339
  _ALGOORDER_EQUALITY._serialized_start=3341
  _ALGOORDER_EQUALITY._serialized_end=3369
  _ALGOORDER_DARKPREFERENCE._serialized_start=3371
  _ALGOORDER_DARKPREFERENCE._serialized_end=3492
# @@protoc_insertion_point(module_scope)
