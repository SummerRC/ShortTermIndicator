# -*- coding: utf-8 -*-
# @Time : 2023/10/16 16:42
# @Author : SummerRC
from db.ecarts_helper import EchartsHelper


class EchartsDataHelper:

    def get_echarts_json_data(self, is_more_data):
        db_helper = EchartsHelper(is_more_data)
        db_helper.connect_to_db()

        # 查询市场情绪数据(按天)
        db_helper.query_index_motion_from_db()
        # 查询市场情绪数据(按分)
        db_helper.query_index_m_motion_from_db()
        # 查询最近40个交易日的综合强度数据
        db_helper.query_zhqd_timestamps_from_db()
        # 查询最近一个交易日当天的综合强度数据
        db_helper.query_most_recent_five_day_zhqds_from_db()
        # 查询连板高度和对应的交易日
        db_helper.query_highest_from_db()
        # 查询昨日涨停溢价
        db_helper.query_ztyj_from_db()

        # 关闭数据库
        db_helper.close_db()

        json = {'timestamps': db_helper.timestamps, 'zhqds': db_helper.zhqds,
                'most_recent_day_zhqds': db_helper.most_recent_trade_day_zhqds,
                'most_recent_day_timestamps': db_helper.most_recent_trade_day_timestamps,
                'trade_day': db_helper.trade_day, 'highest': db_helper.highest, "num_lianban": db_helper.num_lianban,
                'rate_fengban': db_helper.rate_fengban,
                'index_motions': db_helper.index_motions, 'index_timestamps': db_helper.index_timestamps,
                'index_m_motions': db_helper.index_m_motions,
                'index_m_timestamps': db_helper.index_m_timestamps,
                'zrztyj': db_helper.zrztyj, 'zrlbyj': db_helper.zrlbyj, 'date_zrztyj': db_helper.date_zrztyj
                }

        return json
