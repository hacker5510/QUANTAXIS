# coding :utf-8

"""
定义一些可以扩展的数据结构

方便序列化/相互转换

"""

import pandas as pd
import numpy as np

from QUANTAXIS.QAUtil import QA_Setting, QA_util_log_info, QA_util_to_json_from_pandas
from QUANTAXIS.QAFetch import QAQuery


class QA_DataStruct_Stock_day():
    '自定义的日线数据结构'

    def __init__(self, DataFrame):
        self.type = 'stock_day'
        self.if_fq = 'bfq'
        self.mongo_coll = QA_Setting.client.quantaxis.stock_day
        self.open = DataFrame['open']
        self.high = DataFrame['high']
        self.low = DataFrame['low']
        self.close = DataFrame['close']
        self.vol = DataFrame['volume']
        self.date = DataFrame['date']
        self.index = DataFrame.index
        self.data = DataFrame
    def to_qfq(self):
        data = QA_DataStruct_Stock_day(QAQuery.QA_fetch_stock_to_fq(self.data))
        data.if_fq = 'qfq'
        return data

    def to_hfq(self):
        data = QA_DataStruct_Stock_day(
            QAQuery.QA_fetch_stock_to_fq(self.data, 'hfq'))
        data.if_fq = 'hfq'
        return data

    def reverse(self):
        return QA_DataStruct_Stock_day(self.data[::-1])

    def show(self):
        return QA_util_log_info(self.data)

    def add_func(self, func, *arg, **kwargs):
        return func(self.data, *arg, **kwargs)

    def to_list(self):
        return np.asarray(self.data).tolist()

    def to_pd(self):
        return self.data

    def to_numpy(self):
        return np.asarray(self.data)

    def to_json(self):
        return QA_util_to_json_from_pandas(self.data)


class QA_DataStruct_Stock_transaction():
    pass


class QA_DataStruct_Stock_xdxr():
    pass


class QA_DataStruct_Market_reply():
    pass


class QA_DataStruct_Market_bid():
    pass


class QA_DataStruct_Market_bid_queue():
    pass


class QA_DataStruct_ARP_account():
    pass


class QA_DataStruct_Quantaxis_error():
    pass
