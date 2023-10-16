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
        timestamps = db_util.get_timestamps()
        zhqds = db_util.get_zhqds()

        # 查询最近一个交易日当天的综合强度数据
        db_util.query_most_recent_trade_day_zhqds_from_db()
        most_recent_day_zhqds = db_util.get_most_recent_day_zhqds()
        most_recent_day_timestamps = db_util.get_most_recent_day_timestamps()

        # 查询连板高度和对应的交易日
        db_util.query_highest_from_db()
        trade_day = db_util.get_trade_day()
        highest = db_util.get_highest()

        # 关闭数据库
        db_util.close_db()

        json = {'timestamps': timestamps, 'zhqds': zhqds,
                'most_recent_day_zhqds': most_recent_day_zhqds,
                'most_recent_day_timestamps': most_recent_day_timestamps,
                'trade_day': trade_day, 'highest': highest}

        return json
