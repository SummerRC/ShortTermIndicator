import configparser
import logging


def singleton(cls):
    # 单下划线的作用是这个变量只能在当前模块里访问,仅仅是一种提示作用
    # 创建一个字典用来保存类的实例对象
    _instance = {}

    def _singleton(*args, **kwargs):
        # 先判断这个类有没有对象
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)  # 创建一个对象,并保存到字典当中
        # 将实例对象返回
        return _instance[cls]

    return _singleton


@singleton
class ConfigHelper(object):

    def __init__(self):
        conf = configparser.ConfigParser()
        conf.read('config.ini')
        is_online = bool(conf.get("DEFAULT", "IS_ONLINE"))
        if is_online is True:
            logging.warning("is_online is True, 生产环境!!!")
            # 生产环境数据库
            config_db_name = "PROD_DATABASE"
        else:
            logging.debug("is_online is False, 开发环境")
            # 开发环境数据库
            config_db_name = "DEV_DATABASE"

        self.db_address = conf.get(config_db_name, 'HOST')
        self.db_port = int(conf.get(config_db_name, 'PORT'))
        self.db_user = conf.get(config_db_name, 'USER')
        self.db_password = conf.get(config_db_name, 'PASSWORD')
        self.db_name = conf.get(config_db_name, 'DBNAME')
        self.db_charset = conf.get(config_db_name, 'CHARSET')
        self.db_table_name_zhqd = conf.get("DB_TABLE_NAME", 'ZHQD')
        self.db_table_name_zhqd_unique = conf.get("DB_TABLE_NAME", 'ZHQD_UNIQUE')
        self.db_table_name_da_ban = conf.get("DB_TABLE_NAME", 'DA_BAN_LIST')

