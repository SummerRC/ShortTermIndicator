# -*- coding: utf-8 -*-
# @Time : 2023/10/16 16:42
# @Author : SummerRC
from DBUtils import DBUtils


class EchartsDataHelper:

    def get_echarts_json_data(self):
        db_util = DBUtils()
        db_util.connect_to_db()

        # 查询最近40个交易日的综合强度数据
        db_util.query_zhqd_timestamps_from_db()
        # 查询最近一个交易日当天的综合强度数据
        db_util.query_most_recent_five_day_zhqds_from_db()
        # 查询连板高度和对应的交易日
        db_util.query_highest_from_db()

        # 关闭数据库
        db_util.close_db()

        json = {'timestamps': db_util.timestamps, 'zhqds': db_util.zhqds,
                'most_recent_day_zhqds': db_util.most_recent_trade_day_zhqds,
                'most_recent_day_timestamps': db_util.most_recent_trade_day_timestamps,
                'trade_day': db_util.trade_day, 'highest': db_util.highest, 'rate_fengban':db_util.rate_fengban}

        return json
