# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pb_firm_msg.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import pb_common_pb2 as pb__common__pb2
import pb_mkt_msg_pb2 as pb__mkt__msg__pb2
try:
  pb__common__pb2 = pb__mkt__msg__pb2.pb__common__pb2
except AttributeError:
  pb__common__pb2 = pb__mkt__msg__pb2.pb_common_pb2

from pb_common_pb2 import *
from pb_mkt_msg_pb2 import *

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11pb_firm_msg.proto\x12\x04omgw\x1a\x0fpb_common.proto\x1a\x10pb_mkt_msg.proto\"\xef\x03\n\x08PB_F_Msg\x12\x0b\n\x03\x64st\x18\x01 \x01(\x0c\x12\x0b\n\x03src\x18\x02 \x01(\x0c\x12\x0b\n\x03sty\x18\x03 \x01(\t\x12%\n\x04type\x18\x04 \x01(\x0e\x32\x17.omgw.PB_F_DataTypeEnum\x12\x1f\n\x05order\x18\x05 \x01(\x0b\x32\x10.omgw.PB_F_Order\x12\x1f\n\x05trade\x18\x06 \x01(\x0b\x32\x10.omgw.PB_F_Trade\x12\x1f\n\x05ordst\x18\x07 \x01(\x0b\x32\x10.omgw.PB_F_OrdSt\x12\"\n\x05\x61pist\x18\x08 \x01(\x0b\x32\x13.omgw.PB_Api_Status\x12\x1b\n\x03req\x18\t \x01(\x0b\x32\x0e.omgw.PB_F_Req\x12\x32\n\x0f\x61\x63\x63ount_balance\x18\n \x01(\x0b\x32\x19.omgw.PB_F_AccountBalance\x12\x0e\n\x06zmq_id\x18\x0b \x01(\t\x12\x34\n\x10\x61\x63\x63ount_snapshot\x18\x0c \x01(\x0b\x32\x1a.omgw.FB_F_AccountSnapshot\x12)\n\tapp_order\x18\r \x01(\x0b\x32\x16.omgw.PB_F_CmmAppOrder\x12#\n\nime_invite\x18\x0e \x01(\x0b\x32\x0f.omgw.PB_F_IMEI\x12\'\n\x0cgreeks_hedge\x18\x0f \x01(\x0b\x32\x11.omgw.PB_F_GREEKS\"\xcb\n\n\nPB_F_Order\x12\r\n\x05seqno\x18\x01 \x01(\x03\x12\x0b\n\x03sym\x18\x02 \x01(\t\x12\x10\n\x08sym_exch\x18\x03 \x01(\t\x12\x10\n\x08\x65xchange\x18\x04 \x01(\t\x12\x0f\n\x07\x61\x63\x63ount\x18\x05 \x01(\t\x12\x10\n\x08strategy\x18\x06 \x01(\t\x12\x0c\n\x04\x62ook\x18\x07 \x01(\t\x12\x14\n\x0cordid_client\x18\x08 \x01(\t\x12\x16\n\x0eordid_internal\x18\t \x01(\t\x12\x16\n\x0eordid_exchange\x18\n \x01(\t\x12\x11\n\torder_prx\x18\x0b \x01(\x01\x12\x11\n\torder_qty\x18\x0c \x01(\x01\x12\x12\n\norder_prxL\x18\r \x01(\x03\x12\x12\n\norder_qtyL\x18\x0e \x01(\x03\x12\x14\n\x0cprice_factor\x18\x0f \x01(\x03\x12!\n\x07sectype\x18\x10 \x01(\x0e\x32\x10.omgw.PB_SecType\x12!\n\x03\x61pi\x18\x11 \x01(\x0e\x32\x14.omgw.PB_ExchApiEnum\x12(\n\x06\x61\x63tion\x18\x12 \x01(\x0e\x32\x18.omgw.PB_OrderActionEnum\x12*\n\x07\x62uysell\x18\x13 \x01(\x0e\x32\x19.omgw.PB_OrderBuySellEnum\x12.\n\topenclose\x18\x14 \x01(\x0e\x32\x1b.omgw.PB_OrderOpenCloseEnum\x12&\n\x05hedge\x18\x15 \x01(\x0e\x32\x17.omgw.PB_OrderHedgeEnum\x12$\n\x04type\x18\x16 \x01(\x0e\x32\x16.omgw.PB_OrderTypeEnum\x12\"\n\x03tif\x18\x17 \x01(\x0e\x32\x15.omgw.PB_OrderTIFEnum\x12*\n\x07session\x18\x18 \x01(\x0e\x32\x19.omgw.PB_OrderSessionEnum\x12\x11\n\ttimestamp\x18\x19 \x01(\t\x12-\n\x0bordermargin\x18\x1a \x01(\x0e\x32\x18.omgw.PB_OrderMarginEnum\x12\x0e\n\x06trader\x18\x1b \x01(\t\x12(\n\x06status\x18\x1c \x01(\x0e\x32\x18.omgw.PB_OrderStatusEnum\x12\x0e\n\x06\x63lient\x18\x1d \x01(\t\x12\x0c\n\x04\x64\x65sk\x18\x1e \x01(\t\x12\x0e\n\x06\x65ntity\x18\x1f \x01(\t\x12\x0c\n\x04\x66low\x18  \x01(\t\x12\r\n\x05group\x18! \x01(\t\x12\x11\n\tportfolio\x18\" \x01(\t\x12\x12\n\nunderlying\x18# \x01(\t\x12\x12\n\ngeneration\x18$ \x01(\x05\x12.\n\tdirection\x18% \x01(\x0e\x32\x1b.omgw.PB_OrderDirectionEnum\x12\x31\n\talgo_para\x18& \x03(\x0b\x32\x1e.omgw.PB_F_Order.AlgoParaEntry\x12\x14\n\x0ctimestamp_ms\x18\' \x01(\x04\x12\x11\n\talgo_type\x18( \x01(\t\x12\x13\n\x0border_value\x18) \x01(\x01\x12\x18\n\x10\x63ommission_scale\x18* \x01(\x01\x12\x10\n\x08leverage\x18+ \x01(\x01\x12\x12\n\nmaker_only\x18, \x01(\x08\x12\x14\n\x0cordid_parent\x18- \x01(\t\x12\x10\n\x08priority\x18. \x01(\x03\x12\x1a\n\x12slippage_tolerance\x18G \x01(\x01\x12#\n\norder_book\x18H \x01(\x0b\x32\x0f.omgw.PB_M_Book\x12$\n\tleg_order\x18\xe9\x07 \x03(\x0b\x32\x10.omgw.PB_F_Order\x1a\x46\n\rAlgoParaEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.omgw.PB_F_PARA_VALUE:\x02\x38\x01\"<\n\x10PB_F_QuotingData\x12\x0c\n\x04mbid\x18\x01 \x01(\x01\x12\x0c\n\x04mask\x18\x02 \x01(\x01\x12\x0c\n\x04theo\x18\x03 \x01(\x01\"\x85\x01\n\x0fPB_F_OptionData\x12\x0f\n\x07theo_iv\x18\x01 \x01(\x01\x12\x15\n\runderlying_mp\x18\x02 \x01(\x01\x12\x0f\n\x07spot_mp\x18\x03 \x01(\x01\x12\r\n\x05\x64\x65lta\x18\x04 \x03(\x01\x12\r\n\x05gamma\x18\x05 \x03(\x01\x12\x0c\n\x04vega\x18\x06 \x03(\x01\x12\r\n\x05theta\x18\x07 \x03(\x01\"B\n\x0ePB_F_TradeLink\x12\x0f\n\x07orderid\x18\x01 \x01(\x04\x12\r\n\x05price\x18\x02 \x01(\x01\x12\x10\n\x08quantity\x18\x03 \x01(\x01\"\xdb\x07\n\nPB_F_Trade\x12\r\n\x05seqno\x18\x01 \x01(\x03\x12\x0b\n\x03sym\x18\x02 \x01(\t\x12\x10\n\x08sym_exch\x18\x03 \x01(\t\x12\x14\n\x0cordid_client\x18\x04 \x01(\t\x12\x16\n\x0eordid_exchange\x18\x05 \x01(\t\x12\x16\n\x0eordid_internal\x18\x06 \x01(\t\x12\x16\n\x0etrdid_exchange\x18\x07 \x01(\t\x12\x11\n\ttrade_prx\x18\x08 \x01(\x01\x12\x11\n\ttrade_qty\x18\t \x01(\x01\x12\x12\n\ntrade_prxL\x18\n \x01(\x03\x12\x12\n\ntrade_qtyL\x18\x0b \x01(\x03\x12\x14\n\x0cprice_factor\x18\x0c \x01(\x03\x12!\n\x03\x61pi\x18\r \x01(\x0e\x32\x14.omgw.PB_ExchApiEnum\x12*\n\x07\x62uysell\x18\x0e \x01(\x0e\x32\x19.omgw.PB_OrderBuySellEnum\x12!\n\x07sectype\x18\x0f \x01(\x0e\x32\x10.omgw.PB_SecType\x12\x11\n\ttimestamp\x18\x10 \x01(\t\x12\x0f\n\x07\x61\x63\x63ount\x18\x11 \x01(\t\x12\x0c\n\x04\x62ook\x18\x12 \x01(\t\x12\x10\n\x08\x65xchange\x18\x13 \x01(\t\x12\x0e\n\x06trader\x18\x14 \x01(\t\x12\x0e\n\x06\x63lient\x18\x15 \x01(\t\x12\x0c\n\x04\x64\x65sk\x18\x16 \x01(\t\x12\x0e\n\x06\x65ntity\x18\x17 \x01(\t\x12\x0c\n\x04\x66low\x18\x18 \x01(\t\x12\r\n\x05group\x18\x19 \x01(\t\x12\x11\n\tportfolio\x18\x1a \x01(\t\x12\x12\n\nunderlying\x18\x1b \x01(\t\x12\x12\n\ngeneration\x18\x1c \x01(\x05\x12.\n\topenclose\x18\x1d \x01(\x0e\x32\x1b.omgw.PB_OrderOpenCloseEnum\x12.\n\tdirection\x18\x1e \x01(\x0e\x32\x1b.omgw.PB_OrderDirectionEnum\x12\x14\n\x0ctimestamp_ms\x18\x1f \x01(\x04\x12\x12\n\ncommission\x18  \x01(\x01\x12\x10\n\x08leverage\x18! \x01(\x01\x12,\n\x0cquoting_data\x18, \x01(\x0b\x32\x16.omgw.PB_F_QuotingData\x12*\n\x0boption_data\x18- \x01(\x0b\x32\x15.omgw.PB_F_OptionData\x12)\n\x0btrade_links\x18. \x03(\x0b\x32\x14.omgw.PB_F_TradeLink\x12\x14\n\x0cordid_parent\x18/ \x01(\t\x12\x17\n\x0fis_client_order\x18\x30 \x01(\x08\x12\x41\n\x13liquidity_indicator\x18\x31 \x01(\x0e\x32$.omgw.PB_TradeLiquidityIndicatorEnum\"\xa5\n\n\nPB_F_OrdSt\x12\r\n\x05seqno\x18\x01 \x01(\x03\x12\x13\n\x0b\x63reate_time\x18\x02 \x01(\t\x12\x13\n\x0bupdate_time\x18\x03 \x01(\t\x12\x0b\n\x03sym\x18\x04 \x01(\t\x12\x10\n\x08sym_exch\x18\x05 \x01(\t\x12\x14\n\x0cordid_client\x18\x06 \x01(\t\x12\x16\n\x0eordid_exchange\x18\x07 \x01(\t\x12\x16\n\x0eordid_internal\x18\x08 \x01(\t\x12!\n\x03\x61pi\x18\t \x01(\x0e\x32\x14.omgw.PB_ExchApiEnum\x12(\n\x06status\x18\n \x01(\x0e\x32\x18.omgw.PB_OrderStatusEnum\x12\x12\n\nstatus_msg\x18\x0b \x01(\t\x12\x11\n\ttimestamp\x18\x0c \x01(\t\x12\x11\n\torder_prx\x18\r \x01(\x01\x12\x11\n\torder_qty\x18\x0e \x01(\x01\x12*\n\x07\x62uysell\x18\x0f \x01(\x0e\x32\x19.omgw.PB_OrderBuySellEnum\x12\x12\n\nfilled_prx\x18\x10 \x01(\x01\x12\x12\n\nfilled_qty\x18\x11 \x01(\x01\x12\x0c\n\x04\x62ook\x18\x12 \x01(\t\x12\x10\n\x08\x63omments\x18\x13 \x01(\t\x12\x10\n\x08\x65xchange\x18\x14 \x01(\t\x12\x0f\n\x07\x61\x63\x63ount\x18\x15 \x01(\t\x12\x0e\n\x06trader\x18\x16 \x01(\t\x12\x16\n\x0eis_child_order\x18\x17 \x01(\x08\x12\x17\n\x0fparent_order_id\x18\x18 \x01(\t\x12\x0b\n\x03src\x18\x19 \x01(\x0c\x12\x0b\n\x03\x64st\x18\x1a \x01(\x0c\x12,\n\norder_type\x18\x1b \x01(\x0e\x32\x18.omgw.PB_GWOrderTypeEnum\x12\x11\n\tchild_num\x18\x1c \x01(\x03\x12\x13\n\x0bordid_child\x18\x1d \x01(\t\x12\x0f\n\x07ref_prx\x18\x1e \x01(\x01\x12\x0e\n\x06\x63lient\x18\x1f \x01(\t\x12\x0c\n\x04\x64\x65sk\x18  \x01(\t\x12\x0e\n\x06\x65ntity\x18! \x01(\t\x12\x0c\n\x04\x66low\x18\" \x01(\t\x12\r\n\x05group\x18# \x01(\t\x12\x11\n\tportfolio\x18$ \x01(\t\x12\x12\n\nunderlying\x18% \x01(\t\x12\x12\n\ngeneration\x18& \x01(\x05\x12.\n\topenclose\x18\' \x01(\x0e\x32\x1b.omgw.PB_OrderOpenCloseEnum\x12.\n\tdirection\x18( \x01(\x0e\x32\x1b.omgw.PB_OrderDirectionEnum\x12\x31\n\talgo_para\x18) \x03(\x0b\x32\x1e.omgw.PB_F_OrdSt.AlgoParaEntry\x12\x14\n\x0ctimestamp_ms\x18* \x01(\x04\x12\x14\n\x0cmk_mid_price\x18+ \x01(\x01\x12,\n\x0cquoting_data\x18, \x01(\x0b\x32\x16.omgw.PB_F_QuotingData\x12*\n\x0boption_data\x18- \x01(\x0b\x32\x15.omgw.PB_F_OptionData\x12\x1a\n\x12order_mquo_bid_prx\x18. \x01(\x01\x12\x1a\n\x12order_mquo_bid_qty\x18/ \x01(\x01\x12\x1a\n\x12order_mquo_ask_prx\x18\x30 \x01(\x01\x12\x1a\n\x12order_mquo_ask_qty\x18\x31 \x01(\x01\x12\x17\n\x0fis_client_order\x18\x32 \x01(\x08\x12\x16\n\x0e\x63reate_time_ms\x18\x33 \x01(\x04\x1a\x46\n\rAlgoParaEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.omgw.PB_F_PARA_VALUE:\x02\x38\x01\"&\n\x08PB_F_Req\x12\r\n\x05seqno\x18\x01 \x01(\x03\x12\x0b\n\x03\x63md\x18\x02 \x01(\t\"b\n\x10PB_F_SpotBalance\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x01(\t\x12\x10\n\x08\x63urrency\x18\x02 \x01(\t\x12\x0c\n\x04\x66ree\x18\x03 \x01(\x01\x12\r\n\x05total\x18\x04 \x01(\x01\x12\x0e\n\x06locked\x18\x05 \x01(\x01\"\x95\x01\n\x12PB_F_FutureBalance\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x01(\t\x12\x10\n\x08\x63urrency\x18\x02 \x01(\t\x12\x0e\n\x06\x65quity\x18\x03 \x01(\x01\x12\x11\n\tavailable\x18\x04 \x01(\x01\x12\x11\n\ttotal_pnl\x18\x05 \x01(\x01\x12\x0e\n\x06margin\x18\x06 \x01(\x01\x12\x16\n\x0emargin_account\x18\x07 \x01(\t\"\x98\x01\n\x13PB_F_FuturePosition\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x01(\t\x12\x10\n\x08\x63urrency\x18\x02 \x01(\t\x12\x0e\n\x06symbol\x18\x03 \x01(\t\x12\x0c\n\x04side\x18\x04 \x01(\t\x12\x10\n\x08quantity\x18\x05 \x01(\x01\x12\x0f\n\x07\x61vg_prx\x18\x06 \x01(\x01\x12\x10\n\x08mark_prx\x18\x07 \x01(\x01\x12\x0b\n\x03pnl\x18\x08 \x01(\x01\"\xb1\x01\n\x13PB_F_OptionPosition\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12\x10\n\x08long_qty\x18\x03 \x01(\x01\x12\x11\n\tshort_qty\x18\x04 \x01(\x01\x12\x12\n\nsettle_prx\x18\x05 \x01(\x01\x12\x14\n\x0cmaturity_day\x18\x06 \x01(\t\x12\x14\n\x0ctimestamp_ms\x18\x07 \x01(\x04\x12\x14\n\x0cinternal_sym\x18\x08 \x01(\t\"\xa0\x02\n\x13PB_F_AccountBalance\x12\r\n\x05seqno\x18\x01 \x01(\x03\x12!\n\x03\x61pi\x18\x02 \x01(\x0e\x32\x14.omgw.PB_ExchApiEnum\x12.\n\x0cspot_balance\x18\x03 \x01(\x0b\x32\x16.omgw.PB_F_SpotBalanceH\x00\x12\x32\n\x0e\x66uture_balance\x18\x04 \x01(\x0b\x32\x18.omgw.PB_F_FutureBalanceH\x00\x12\x34\n\x0f\x66uture_position\x18\x05 \x01(\x0b\x32\x19.omgw.PB_F_FuturePositionH\x00\x12\x34\n\x0foption_position\x18\x06 \x01(\x0b\x32\x19.omgw.PB_F_OptionPositionH\x00\x42\x07\n\x05\x61sset\"\xdc\x01\n\x14\x46\x42_F_AccountSnapshot\x12\r\n\x05seqno\x18\x01 \x01(\x03\x12!\n\x03\x61pi\x18\x02 \x01(\x0e\x32\x14.omgw.PB_ExchApiEnum\x12,\n\x0cspot_balance\x18\x03 \x03(\x0b\x32\x16.omgw.PB_F_SpotBalance\x12\x30\n\x0e\x66uture_balance\x18\x04 \x03(\x0b\x32\x18.omgw.PB_F_FutureBalance\x12\x32\n\x0f\x66uture_position\x18\x05 \x03(\x0b\x32\x19.omgw.PB_F_FuturePosition\"%\n\x07PB_F_KV\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\")\n\tPB_F_LIST\x12\x1c\n\x05value\x18\x01 \x03(\x0b\x32\r.omgw.PB_F_KV\"b\n\x08PB_F_MAP\x12(\n\x05value\x18\x01 \x03(\x0b\x32\x19.omgw.PB_F_MAP.ValueEntry\x1a,\n\nValueEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"{\n\x0fPB_F_PARA_VALUE\x12\x13\n\tvalue_str\x18\x01 \x01(\tH\x00\x12#\n\tvalue_map\x18\x02 \x01(\x0b\x32\x0e.omgw.PB_F_MAPH\x00\x12%\n\nvalue_list\x18\x03 \x01(\x0b\x32\x0f.omgw.PB_F_LISTH\x00\x42\x07\n\x05value\"\xcb\x07\n\x10PB_F_CmmAppOrder\x12\x0c\n\x04\x61\x63\x63t\x18\x01 \x01(\t\x12\x10\n\x08strategy\x18\x02 \x01(\t\x12\x0c\n\x04\x62ook\x18\x03 \x01(\t\x12\x11\n\thedge_sym\x18\x04 \x01(\t\x12\x0f\n\x07\x63omment\x18\x05 \x01(\t\x12\x10\n\x08\x65word_id\x18\x06 \x01(\t\x12\x13\n\x0btime_create\x18\x07 \x01(\t\x12\x13\n\x0btime_update\x18\x08 \x01(\t\x12\x10\n\x08\x62\x61se_sym\x18\x0b \x01(\t\x12\x10\n\x08\x62\x61se_prx\x18\x0c \x01(\x01\x12\x10\n\x08\x62\x61se_qty\x18\r \x01(\x01\x12\x10\n\x08open_qty\x18\x0e \x01(\x01\x12\x11\n\torder_sym\x18\x15 \x01(\t\x12\x15\n\rorder_buysell\x18\x16 \x01(\t\x12\x10\n\x08order_id\x18\x17 \x01(\t\x12\x19\n\x11order_id_exchange\x18\x18 \x01(\t\x12\x11\n\torder_prx\x18\x19 \x01(\x01\x12\x11\n\torder_qty\x18\x1a \x01(\x01\x12\x14\n\x0corder_status\x18\x1b \x01(\t\x12\x14\n\x0cordid_client\x18\x1c \x01(\t\x12\x10\n\x08trade_id\x18\x1d \x01(\t\x12\x10\n\x08\x66ill_prx\x18\x1e \x01(\x01\x12\x10\n\x08\x66ill_qty\x18\x1f \x01(\x01\x12\x15\n\rquote_buysell\x18) \x01(\t\x12\x11\n\tquote_prx\x18* \x01(\x01\x12\x11\n\tquote_qty\x18+ \x01(\x01\x12\x11\n\tquote_sym\x18, \x01(\t\x12\x12\n\nquote_type\x18- \x01(\t\x12\x14\n\x0ctrans_amount\x18\x33 \x01(\x01\x12\x18\n\x10trans_created_at\x18\x34 \x01(\t\x12\x19\n\x11trans_from_amount\x18\x35 \x01(\x01\x12\x1b\n\x13trans_from_currency\x18\x36 \x01(\t\x12\x1a\n\x12trans_hedge_status\x18\x37 \x01(\t\x12\x1c\n\x14trans_hedge_trade_id\x18\x38 \x01(\t\x12\x10\n\x08trans_id\x18\x39 \x01(\x04\x12\"\n\x1atrans_order_execution_time\x18: \x01(\t\x12\x1d\n\x15trans_quote_engine_id\x18; \x01(\t\x12\x12\n\ntrans_rate\x18< \x01(\x01\x12\x16\n\x0etrans_rate_sym\x18= \x01(\t\x12\x1c\n\x14trans_rate_timestamp\x18> \x01(\x04\x12\x11\n\ttrans_src\x18? \x01(\t\x12\x19\n\x11trans_to_currency\x18@ \x01(\t\x12\x18\n\x10trans_updated_at\x18\x41 \x01(\t\x12\x15\n\rtrans_user_id\x18\x42 \x01(\x04\"\xc9\x01\n\tPB_F_IMEI\x12/\n\x05value\x18\x01 \x03(\x0b\x32 .omgw.PB_F_IMEI.PB_F_Invitiation\x1a\x8a\x01\n\x10PB_F_Invitiation\x12\x16\n\x0eordid_internal\x18\x01 \x01(\t\x12\x14\n\x0cordid_client\x18\x02 \x01(\t\x12\x10\n\x08quantity\x18\x03 \x01(\x01\x12\x11\n\ttimestamp\x18\x04 \x01(\t\x12\x14\n\x0ctimestamp_ms\x18\x05 \x01(\x04\x12\r\n\x05seqno\x18\x06 \x01(\x03\"\x8d\x03\n\x0bPB_F_GREEKS\x12\r\n\x05seqno\x18\x01 \x01(\x03\x12\x11\n\ttimestamp\x18\x02 \x01(\x04\x12\r\n\x05\x64\x65lta\x18\n \x01(\x01\x12\r\n\x05gamma\x18\x0b \x01(\x01\x12\x0c\n\x04vega\x18\x0c \x01(\x01\x12\r\n\x05theta\x18\r \x01(\x01\x12\x0b\n\x03rho\x18\x0e \x01(\x01\x12\x14\n\x0c\x64ollar_delta\x18\x14 \x01(\x01\x12\x14\n\x0c\x64ollar_gamma\x18\x15 \x01(\x01\x12\x13\n\x0b\x64ollar_vega\x18\x16 \x01(\x01\x12\x14\n\x0c\x64ollar_theta\x18\x17 \x01(\x01\x12\x12\n\ndollar_rho\x18\x18 \x01(\x01\x12\x1f\n\x05trade\x18\x1e \x01(\x0b\x32\x10.omgw.PB_F_Trade\x12\x0e\n\x06symbol\x18\x1f \x01(\t\x12\x10\n\x08\x65xchange\x18  \x01(\t\x12\x0f\n\x07\x61\x63\x63ount\x18! \x01(\t\x12\x10\n\x08strategy\x18\" \x01(\t\x12\x0c\n\x04\x62ook\x18# \x01(\t\x12\x11\n\tportfolio\x18$ \x01(\t\x12\x12\n\nunderlying\x18% \x01(\t\x12\x0e\n\x06source\x18& \x01(\t*g\n\x11PB_F_DataTypeEnum\x12\n\n\x06\x46Order\x10\x00\x12\n\n\x06\x46Trade\x10\x01\x12\n\n\x06\x46OrdSt\x10\x02\x12\n\n\x06\x46\x41PISt\x10\x03\x12\x08\n\x04\x46Req\x10\x04\x12\r\n\tFAppOrder\x10\x05\x12\t\n\x05\x46IMEI\x10\x06\x42\x03\xf8\x01\x01P\x00P\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pb_firm_msg_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\370\001\001'
  _PB_F_ORDER_ALGOPARAENTRY._options = None
  _PB_F_ORDER_ALGOPARAENTRY._serialized_options = b'8\001'
  _PB_F_ORDST_ALGOPARAENTRY._options = None
  _PB_F_ORDST_ALGOPARAENTRY._serialized_options = b'8\001'
  _PB_F_MAP_VALUEENTRY._options = None
  _PB_F_MAP_VALUEENTRY._serialized_options = b'8\001'
  _PB_F_DATATYPEENUM._serialized_start=7520
  _PB_F_DATATYPEENUM._serialized_end=7623
  _PB_F_MSG._serialized_start=63
  _PB_F_MSG._serialized_end=558
  _PB_F_ORDER._serialized_start=561
  _PB_F_ORDER._serialized_end=1916
  _PB_F_ORDER_ALGOPARAENTRY._serialized_start=1846
  _PB_F_ORDER_ALGOPARAENTRY._serialized_end=1916
  _PB_F_QUOTINGDATA._serialized_start=1918
  _PB_F_QUOTINGDATA._serialized_end=1978
  _PB_F_OPTIONDATA._serialized_start=1981
  _PB_F_OPTIONDATA._serialized_end=2114
  _PB_F_TRADELINK._serialized_start=2116
  _PB_F_TRADELINK._serialized_end=2182
  _PB_F_TRADE._serialized_start=2185
  _PB_F_TRADE._serialized_end=3172
  _PB_F_ORDST._serialized_start=3175
  _PB_F_ORDST._serialized_end=4492
  _PB_F_ORDST_ALGOPARAENTRY._serialized_start=1846
  _PB_F_ORDST_ALGOPARAENTRY._serialized_end=1916
  _PB_F_REQ._serialized_start=4494
  _PB_F_REQ._serialized_end=4532
  _PB_F_SPOTBALANCE._serialized_start=4534
  _PB_F_SPOTBALANCE._serialized_end=4632
  _PB_F_FUTUREBALANCE._serialized_start=4635
  _PB_F_FUTUREBALANCE._serialized_end=4784
  _PB_F_FUTUREPOSITION._serialized_start=4787
  _PB_F_FUTUREPOSITION._serialized_end=4939
  _PB_F_OPTIONPOSITION._serialized_start=4942
  _PB_F_OPTIONPOSITION._serialized_end=5119
  _PB_F_ACCOUNTBALANCE._serialized_start=5122
  _PB_F_ACCOUNTBALANCE._serialized_end=5410
  _FB_F_ACCOUNTSNAPSHOT._serialized_start=5413
  _FB_F_ACCOUNTSNAPSHOT._serialized_end=5633
  _PB_F_KV._serialized_start=5635
  _PB_F_KV._serialized_end=5672
  _PB_F_LIST._serialized_start=5674
  _PB_F_LIST._serialized_end=5715
  _PB_F_MAP._serialized_start=5717
  _PB_F_MAP._serialized_end=5815
  _PB_F_MAP_VALUEENTRY._serialized_start=5771
  _PB_F_MAP_VALUEENTRY._serialized_end=5815
  _PB_F_PARA_VALUE._serialized_start=5817
  _PB_F_PARA_VALUE._serialized_end=5940
  _PB_F_CMMAPPORDER._serialized_start=5943
  _PB_F_CMMAPPORDER._serialized_end=6914
  _PB_F_IMEI._serialized_start=6917
  _PB_F_IMEI._serialized_end=7118
  _PB_F_IMEI_PB_F_INVITIATION._serialized_start=6980
  _PB_F_IMEI_PB_F_INVITIATION._serialized_end=7118
  _PB_F_GREEKS._serialized_start=7121
  _PB_F_GREEKS._serialized_end=7518
# @@protoc_insertion_point(module_scope)
