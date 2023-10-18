# -*- coding: utf-8 -*-
# @Time : 2023/10/18 12:03
# @Author : SummerRC
import logging

from static.db.base_ecarts_helper import BaseEchartsHelper
from utils.stock_utils import StockUtils


class EchartsHelper(BaseEchartsHelper):

    def __init__(self, is_more):
        super().__init__(is_more)

    # 查询的是最近100个交易日的数据
    def query_zhqd_timestamps_from_db(self):
        # 查询出数据之后按照 index 值降序排序，并获取前40条
        sql = ("select zhqd, timestamp, is_trade_time, data_crawl_timestamp, id from %s \
                     WHERE is_trade_time = 0 ORDER BY id DESC LIMIT %s " %
               (self.config_helper.db_table_name_zhqd_unique, self.num_zhqd))

        try:
            self.cursor.execute(sql)
        except Exception as e:
            logging.log(logging.ERROR, str(e))

        self.zhqds.clear()
        self.timestamps.clear()
        self.zhqd_timestamps.clear()

        results = self.cursor.fetchall()
        for result in results:
            self.zhqds.append(result[0])
            # 去前置0的操作
            tm = result[1].timetuple()
            timestamp = str(tm.tm_mon) + str(tm.tm_mday)
            self.timestamps.append(timestamp)
            logging.log(logging.DEBUG, "zhqd: " + str(result[0]))
            logging.log(logging.DEBUG, "去前置0后的timestamps: " + timestamp)

        self.zhqd_timestamps.append((self.zhqds,  self.timestamps))

        self.zhqds.reverse()
        self.timestamps.reverse()
        self.zhqd_timestamps.reverse()

    # 查询的是最近一个交易日的数据，以分钟计算
    def query_most_recent_five_day_zhqds_from_db(self):
        json_data = StockUtils.get_most_num_trade_day(self.num_recent_zhqd)

        # 查询出数据之后按照 index 值降序排序，并获取前60条
        sql = ("select zhqd, timestamp, is_trade_time, data_crawl_timestamp, id from %s \
             WHERE timestamp BETWEEN '%s' AND '%s'" %
               (self.config_helper.db_table_name_zhqd_unique, json_data.get('start_time'), json_data.get('end_time')))

        try:
            self.cursor.execute(sql)
        except Exception as e:
            logging.log(logging.ERROR, str(e))

        self.most_recent_trade_day_zhqds.clear()
        self.most_recent_trade_day_timestamps.clear()

        results = self.cursor.fetchall()
        for result in results:
            self.most_recent_trade_day_zhqds.append(result[0])
            # 只保留时、分
            timestamp = str(result[1].hour) + ":" + str(result[1].minute)
            self.most_recent_trade_day_timestamps.append(timestamp)
            logging.log(logging.DEBUG, "zhqd: " + str(result[0]))
            logging.log(logging.DEBUG, "去日期后的timestamps: " + timestamp)

    # 查询最高板、封板率
    def query_highest_from_db(self):
        # 查询出数据之后按照 index 值降序排序，并获取前60条
        sql = ("select trade_day, high_lianban, rate_fengban from %s ORDER BY trade_day DESC LIMIT %s" %
               (self.config_helper.db_tn_tdx_history_zdt, self.num_highest))

        try:
            self.cursor.execute(sql)
        except Exception as e:
            logging.log(logging.ERROR, "query_highest_from_db() error: " + str(e))

        self.highest.clear()
        self.trade_day.clear()
        self.rate_fengban.clear()

        results = self.cursor.fetchall()
        for result in results:
            self.trade_day.append(result[0])
            self.highest.append(result[1])
            self.rate_fengban.append(result[2])

        self.trade_day.reverse()
        self.highest.reverse()
        self.rate_fengban.reverse()

