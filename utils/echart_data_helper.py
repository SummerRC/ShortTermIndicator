# -*- coding: utf-8 -*-
# @Time : 2023/10/16 16:42
# @Author : SummerRC
from static.db.ecarts_helper import EchartsHelper


class EchartsDataHelper:

    def get_echarts_json_data(self, is_more=True):
        echarts_helper = EchartsHelper(is_more)
        echarts_helper.connect_to_db()

        # 查询最近40个交易日的综合强度数据
        echarts_helper.query_zhqd_timestamps_from_db()
        # 查询最近一个交易日当天的综合强度数据
        echarts_helper.query_most_recent_five_day_zhqds_from_db()
        # 查询连板高度和对应的交易日
        echarts_helper.query_highest_from_db()

        # 关闭数据库
        echarts_helper.close_db()

        json = {'timestamps': echarts_helper.timestamps, 'zhqds': echarts_helper.zhqds,
                'most_recent_day_zhqds': echarts_helper.most_recent_trade_day_zhqds,
                'most_recent_day_timestamps': echarts_helper.most_recent_trade_day_timestamps,
                'trade_day': echarts_helper.trade_day, 'highest': echarts_helper.highest,
                'rate_fengban': echarts_helper.rate_fengban}

        return json
