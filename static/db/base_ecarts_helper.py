# -*- coding: utf-8 -*-
# @Time : 2023/10/18 12:03
# @Author : SummerRC

import pymysql
from utils.config_helper import ConfigHelper


class BaseEchartsHelper:
    zhqds = []
    timestamps = []
    zhqd_timestamps = []

    most_recent_trade_day_zhqds = []
    most_recent_trade_day_timestamps = []

    highest = []
    trade_day = []
    rate_fengban = []

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
        else:
            self.num_zhqd = self.config_helper.num_zhqd_less
            self.num_recent_zhqd = self.config_helper.num_recent_zhqd_less
            self.num_highest = self.config_helper.num_highest_less

    def connect_to_db(self):
        self.conn = pymysql.connect(host=self.config_helper.db_address, port=self.config_helper.db_port,
                                    user=self.config_helper.db_user, password=self.config_helper.db_password,
                                    database=self.config_helper.db_name, charset=self.config_helper.db_charset)
        self.cursor = self.conn.cursor()

    def close_db(self):
        self.conn.close()
