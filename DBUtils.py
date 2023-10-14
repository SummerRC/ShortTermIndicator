
import logging
import configparser

import pymysql


class DBUtils:
    zhqds = []
    timestamps = []
    zhqd_timestamps = []

    def __init__(self):
        conf = configparser.ConfigParser()
        conf.read('config.ini')
        config_db_name = 'PROD_DATABASE'
        # config_db_name = 'DEV_DATABASE'
        db_address = conf.get(config_db_name, 'HOST')
        db_port = int(conf.get(config_db_name, 'PORT'))
        db_user = conf.get(config_db_name, 'USER')
        db_password = conf.get(config_db_name, 'PASSWORD')
        db_name = conf.get(config_db_name, 'DBNAME')
        db_charset = conf.get(config_db_name, 'CHARSET')

        self.conn = pymysql.connect(host=db_address, port=db_port, user=db_user, password=db_password, database=db_name,
                                    charset=db_charset)

        self.cursor = self.conn.cursor()

    def refresh_zhqd_timestamps_from_db(self):
        # 查询出数据之后按照 index 值降序排序，并获取前60条
        sql = """select zhqd, timestamp, is_trade_time, data_crawl_timestamp, id from kaipanla_zhqd_unique \
             WHERE is_trade_time = 0 ORDER BY id DESC LIMIT 40 """

        cursor = self.cursor
        try:
            cursor.execute(sql)
        except Exception as e:
            print(e)

        self.zhqds.clear()
        self.timestamps.clear()
        self.zhqd_timestamps.clear()

        results = cursor.fetchall()
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

    def get_zhqds(self):
        return self.zhqds

    def get_timestamps(self):
        return self.timestamps

