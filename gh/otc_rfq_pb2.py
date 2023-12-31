# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: otc_rfq.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import otc_common_pb2 as otc__common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rotc_rfq.proto\x12\x0estrategy_proto\x1a\x10otc_common.proto\"\x96\r\n\x07OTC_RFQ\x12\x10\n\x08\x62\x61se_ccy\x18\x01 \x01(\t\x12\x11\n\tquote_ccy\x18\x02 \x01(\t\x12\x15\n\rbase_ccy_size\x18\x03 \x01(\x01\x12\x16\n\x0equote_ccy_size\x18\x04 \x01(\x01\x12\x34\n\tdirection\x18\x05 \x01(\x0e\x32!.strategy_proto.OTCQuoteDirection\x12\x0e\n\x06status\x18\x06 \x01(\x05\x12\x14\n\x0c\x65rror_reason\x18\x07 \x01(\t\x12\x15\n\rclient_rfq_id\x18\n \x01(\t\x12\x16\n\x0etrading_rfq_id\x18\x0b \x01(\t\x12\x17\n\x0f\x63lient_identity\x18\x0c \x01(\t\x12\x19\n\x11request_timestamp\x18\x14 \x01(\x04\x12\x17\n\x0fquote_timestamp\x18\x15 \x01(\x04\x12\x18\n\x10\x65xpiry_timestamp\x18\x16 \x01(\x04\x12\x16\n\x0equote_duration\x18\x17 \x01(\x01\x12\x11\n\tbuy_quote\x18\x1e \x01(\x01\x12\x12\n\nsell_quote\x18\x1f \x01(\x01\x12\x0f\n\x07ref_prx\x18  \x01(\x01\x12\x11\n\tclient_id\x18( \x01(\t\x12\x10\n\x08sales_id\x18) \x01(\t\x12)\n\x08otc_flow\x18+ \x01(\x0e\x32\x17.strategy_proto.OTCFlow\x12\x17\n\x0ftrade_on_credit\x18, \x01(\x08\x12\x1a\n\x12is_quote_ccy_quote\x18- \x01(\x08\x12\x10\n\x08\x62\x61se_bid\x18\x33 \x01(\x01\x12\x10\n\x08\x62\x61se_ask\x18\x34 \x01(\x01\x12\x10\n\x08last_prx\x18\x35 \x01(\x01\x12\x17\n\x0freal_margin_bid\x18\x36 \x01(\x01\x12\x17\n\x0freal_margin_ask\x18\x37 \x01(\x01\x12\x13\n\x0bsymbol_root\x18< \x01(\t\x12\x11\n\ttier_type\x18= \x01(\t\x12\x13\n\x0btier_margin\x18? \x01(\x01\x12\x17\n\x0fis_default_tier\x18@ \x01(\x08\x12\x16\n\x0e\x62id_vol_margin\x18\x41 \x01(\x01\x12\x16\n\x0e\x61sk_vol_margin\x18\x42 \x01(\x01\x12\x13\n\x0bmode_margin\x18\x44 \x01(\x01\x12\x12\n\nis_expired\x18\x46 \x01(\x08\x12\x17\n\x0f\x62uffer_duration\x18G \x01(\x01\x12\x15\n\rmanual_margin\x18I \x01(\x01\x12\x12\n\ncap_margin\x18J \x01(\x01\x12\x17\n\x0f\x62\x61se_margin_bid\x18K \x01(\x01\x12\x17\n\x0f\x62\x61se_margin_ask\x18L \x01(\x01\x12\x17\n\x0ftier_1_margin_a\x18M \x01(\x01\x12\x17\n\x0ftier_1_margin_b\x18N \x01(\x01\x12\x19\n\x11tier_1_margin_bid\x18O \x01(\x01\x12\x19\n\x11tier_1_margin_ask\x18P \x01(\x01\x12\x18\n\x10\x66inal_margin_bid\x18Q \x01(\x01\x12\x18\n\x10\x66inal_margin_ask\x18R \x01(\x01\x12\x18\n\x10total_margin_bid\x18S \x01(\x01\x12\x18\n\x10total_margin_ask\x18T \x01(\x01\x12\x11\n\tt_account\x18U \x01(\t\x12\x0e\n\x06t_book\x18V \x01(\t\x12\x12\n\nt_strategy\x18W \x01(\t\x12\x10\n\x08t_trader\x18X \x01(\t\x12\r\n\x05r_src\x18Y \x01(\t\x12\x1a\n\x12\x63lient_tier_margin\x18Z \x01(\x01\x12\x19\n\x11sales_tier_margin\x18[ \x01(\x01\x12\x19\n\x11\x63lient_tier_level\x18\\ \x01(\x05\x12\x18\n\x10sales_tier_level\x18] \x01(\x05\x12\x15\n\rotc_flow_type\x18^ \x01(\t\x12\x15\n\rtr_margin_bid\x18_ \x01(\x01\x12\x15\n\rtr_margin_ask\x18` \x01(\x01\x12\x16\n\x0etarget_qty_bid\x18\x61 \x01(\x01\x12\x16\n\x0etarget_qty_ask\x18\x62 \x01(\x01\x12\x17\n\x0f\x63umulative_risk\x18\x63 \x01(\x01\x12\x19\n\x11s_step_margin_bid\x18\x64 \x01(\x01\x12\x19\n\x11s_step_margin_ask\x18\x65 \x01(\x01\x12\x1b\n\x13s_cap_manual_margin\x18\x66 \x01(\x01\x12\x19\n\x11s_bid_manual_mgin\x18g \x01(\x01\x12\x19\n\x11s_ask_manual_mgin\x18h \x01(\x01\x12\x15\n\rcredit_margin\x18i \x01(\x01J\x04\x08\x43\x10\x44J\x04\x08\x32\x10\x33R\ttr_marginR\ntarget_qty\"\xfb\x04\n\x10OTC_RFQ_RESPONSE\x12\x10\n\x08\x62\x61se_ccy\x18\x01 \x01(\t\x12\x11\n\tquote_ccy\x18\x02 \x01(\t\x12\x15\n\rbase_ccy_size\x18\x03 \x01(\x01\x12\x16\n\x0equote_ccy_size\x18\x04 \x01(\x01\x12\x34\n\tdirection\x18\x05 \x01(\x0e\x32!.strategy_proto.OTCQuoteDirection\x12\x0e\n\x06status\x18\x06 \x01(\x05\x12\x14\n\x0c\x65rror_reason\x18\x07 \x01(\t\x12\x15\n\rclient_rfq_id\x18\n \x01(\t\x12\x16\n\x0etrading_rfq_id\x18\x0b \x01(\t\x12\x17\n\x0f\x63lient_identity\x18\x0c \x01(\t\x12\x19\n\x11request_timestamp\x18\x14 \x01(\x04\x12\x17\n\x0fquote_timestamp\x18\x15 \x01(\x04\x12\x18\n\x10\x65xpiry_timestamp\x18\x16 \x01(\x04\x12\x16\n\x0equote_duration\x18\x17 \x01(\x01\x12\x11\n\tbuy_quote\x18\x1e \x01(\x01\x12\x12\n\nsell_quote\x18\x1f \x01(\x01\x12\x11\n\tclient_id\x18( \x01(\t\x12\x10\n\x08sales_id\x18) \x01(\t\x12\x14\n\x0csales_margin\x18* \x01(\x01\x12)\n\x08otc_flow\x18+ \x01(\x0e\x32\x17.strategy_proto.OTCFlow\x12\x17\n\x0ftrade_on_credit\x18, \x01(\x08\x12\x1a\n\x12is_quote_ccy_quote\x18- \x01(\x08\x12\x11\n\tt_account\x18. \x01(\t\x12\x0e\n\x06t_book\x18/ \x01(\t\x12\x12\n\nt_strategy\x18\x30 \x01(\t\x12\x10\n\x08t_trader\x18\x31 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'otc_rfq_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _OTC_RFQ._serialized_start=52
  _OTC_RFQ._serialized_end=1738
  _OTC_RFQ_RESPONSE._serialized_start=1741
  _OTC_RFQ_RESPONSE._serialized_end=2376
# @@protoc_insertion_point(module_scope)
