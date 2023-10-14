
import logging
import pymysql

from utils.config_helper import ConfigHelper
from utils.stock_utils import StockUtils


class DBUtils:
    zhqds = []
    timestamps = []
    zhqd_timestamps = []

    most_recent_trade_day_zhqds = []
    most_recent_trade_day_timestamps = []

    def __init__(self):
        self.config_helper = ConfigHelper()

    def __connect_to_db(self):
        self.conn = pymysql.connect(host=self.config_helper.db_address, port=self.config_helper.db_port,
                                    user=self.config_helper.db_user, password=self.config_helper.db_password,
                                    database=self.config_helper.db_name, charset=self.config_helper.db_charset)
        self.cursor = self.conn.cursor()

    # 查询的是最近40个交易日的数据
    def query_zhqd_timestamps_from_db(self):
        self.__connect_to_db()

        # 查询出数据之后按照 index 值降序排序，并获取前60条
        sql = "select zhqd, timestamp, is_trade_time, data_crawl_timestamp, id from %s \
                     WHERE is_trade_time = 0 ORDER BY id DESC LIMIT 40 " % self.config_helper.db_table_name_zhqd_unique

        try:
            self.cursor.execute(sql)
        except Exception as e:
            print(e)

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

        self.conn.close()

    # 查询的是最近一个交易日的数据，以分钟计算
    def query_most_recent_trade_day_zhqds_from_db(self):
        self.__connect_to_db()

        most_recent_trade_day = StockUtils.get_most_recent_trade_day(self)
        # 查询出数据之后按照 index 值降序排序，并获取前60条
        sql = "select zhqd, timestamp, is_trade_time, data_crawl_timestamp, id from %s \
             WHERE is_trade_time = 1 ORDER BY id DESC LIMIT 40 " % self.config_helper.db_table_name_zhqd_unique

        try:
            self.cursor.execute(sql)
        except Exception as e:
            print(e)

        self.most_recent_trade_day_zhqds.clear()
        self.most_recent_trade_day_timestamps.clear()

        results = self.cursor.fetchall()
        for result in results:
            self.most_recent_trade_day_zhqds.append(result[0])
            # 只保留时分秒
            timestamp = str(result[1].hour) + str(result[1].minute)
            self.most_recent_trade_day_timestamps.append(timestamp)
            logging.log(logging.DEBUG, "zhqd: " + str(result[0]))
            logging.log(logging.DEBUG, "去日期后的timestamps: " + timestamp)

        self.most_recent_trade_day_zhqds.reverse()
        self.most_recent_trade_day_timestamps.reverse()

        self.conn.close()

    def get_zhqds(self):
        return self.zhqds

    def get_timestamps(self):
        return self.timestamps

    def get_most_recent_day_zhqds(self):
        return self.most_recent_trade_day_zhqds

    def get_most_recent_day_timestamps(self):
        return self.most_recent_trade_day_timestamps

