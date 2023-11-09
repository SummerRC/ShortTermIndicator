# -*- coding: utf-8 -*-
# @Time : 2023/10/18 12:03
# @Author : SummerRC

import pymysql
from utils.config_helper import ConfigHelper


class BaseEchartsHelper:
    # 指数情绪（按日）
    index_motions = []
    index_timestamps = []

    # 指数情绪（按分钟）
    index_m_motions = []
    index_m_timestamps = []

    zhqds = []
    timestamps = []
    zhqd_timestamps = []

    most_recent_trade_day_zhqds = []
    most_recent_trade_day_timestamps = []

    highest = []
    trade_day = []
    rate_fengban = []
    num_lianban = []

    #昨日涨停/连板溢价率
    zrztyj = []
    zrlbyj = []
    date_zrztyj = []

    def __init__(self, is_more_data):
        self.cursor = None
        self.conn = None
        self.config_helper = ConfigHelper()
        self.is_more_data = is_more_data
        self.__init_config()

    def __init_config(self):
        if self.is_more_data:
            self.num_zhqd = self.config_helper.num_zhqd_more
            self.num_recent_zhqd = self.config_helper.num_recent_zhqd_more
            self.num_highest = self.config_helper.num_highest_more
            self.num_index_motion = self.config_helper.num_index_motion_more
            self.num_motion_m = self.config_helper.num_motion_m_more
        else:
            self.num_zhqd = self.config_helper.num_zhqd_less
            self.num_recent_zhqd = self.config_helper.num_recent_zhqd_less
            self.num_highest = self.config_helper.num_highest_less
            self.num_index_motion = self.config_helper.num_index_motion_less
            self.num_motion_m = self.config_helper.num_motion_m_less

    def connect_to_db(self):
        self.conn = pymysql.connect(host=self.config_helper.db_address, port=self.config_helper.db_port,
                                    user=self.config_helper.db_user, password=self.config_helper.db_password,
                                    database=self.config_helper.db_name, charset=self.config_helper.db_charset)
        self.cursor = self.conn.cursor()

    def close_db(self):
        self.conn.close()
