# -*- coding: utf-8 -*-
# @Time : 2023/10/16 16:42
# @Author : SummerRC
from db.ecarts_helper import EchartsHelper


class EchartsDataHelper:

    def get_echarts_json_data(self, is_more_data):
        echarts_helper = EchartsHelper(is_more_data)
        echarts_helper.connect_to_db()

        # 查询市场情绪数据(按天)
        echarts_helper.query_index_motion_from_db()
        # 查询市场情绪数据(按分)
        echarts_helper.query_index_m_motion_from_db()
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
                'rate_fengban': echarts_helper.rate_fengban,
                'index_motions': echarts_helper.index_motions, 'index_timestamps': echarts_helper.index_timestamps,
                'index_m_motions': echarts_helper.index_m_motions,
                'index_m_timestamps': echarts_helper.index_m_timestamps,
                }

        return json
