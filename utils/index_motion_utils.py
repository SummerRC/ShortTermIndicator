import logging

__A_MIN__ = -80
__A_MAX__ = 80
__B_MIN__ = 10
__B_MAX__ = 90
__C_MIN__ = -40
__C_MAX__ = 40
__TOTAL_MIN__ = __A_MIN__ + __B_MIN__ + __C_MIN__
__TOTAL_MAX__ = __A_MAX__ + __B_MAX__ + __C_MAX__


class IndexMotionUtils:

    # 指数情绪的计算方法
    # 2.指数情绪量化（以下数字之和,范围[-110:210] ）: ( (a+b+c)-(-110) ) * 100 / (210-(-110))
    #       a.指数涨跌幅 * 2000 [-80:80]
    #       b.上涨家数占比 * 100 [10:90]
    #       c.(市场成交额 - 0.9万亿) / 1e10 [-40:40]

    @staticmethod
    def get_index_motion(a, b, c):
        result = int(((a + b + c) - __TOTAL_MIN__) * 100 / (__TOTAL_MAX__ - __TOTAL_MIN__))
        # logging.log(logging.DEBUG, "get_index_motion: " + str(result))
        return result

    # 获取指数涨跌幅
    # 注意，是 shang_zhen_zhi_shu 存储的是0.xx ，代表的是 0.xx% ，所以要先/100
    @staticmethod
    def get_a_index_zdf(shang_zhen_zhi_shu):
        result = shang_zhen_zhi_shu / 100 * 2000
        # logging.log(logging.DEBUG, "get_a_index_zdf: " + str(result))
        if result > __A_MAX__:
            return __A_MAX__
        elif result < __A_MIN__:
            return __A_MIN__
        else:
            return result

    # 获取上涨家数占比
    @staticmethod
    def get_b_rate_szjs(SZJS, XDJS, PPJS):
        result = SZJS / (SZJS + XDJS + PPJS) * 100
        # logging.log(logging.DEBUG, "get_b_rate_szjs: " + str(result))
        if result > __B_MAX__:
            return __B_MAX__
        elif result < __B_MIN__:
            return __B_MIN__
        else:
            return result

    # 获取市场成交额
    # total_trade_money: 单位是亿，因此需要x10e8,再/10e10 == /100
    @staticmethod
    def get_c_trade_money(total_trade_money):
        result = (total_trade_money - 9000) / 100
        # logging.log(logging.DEBUG, "get_c_trade_money: " + str(result))
        if result > __C_MAX__:
            return __C_MAX__
        elif result < __C_MIN__:
            return __C_MIN__
        else:
            return result

