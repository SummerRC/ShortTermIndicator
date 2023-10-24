import logging


class IndexMotionUtils:

    # 指数情绪的计算方法
    # 2.指数情绪量化（以下数字之和,范围[-110:210] ）: ( (a+b+c)-(-110) ) * 100 / (210-(-110))
    #       a.指数涨跌幅 * 2000 [-80:80]
    #       b.上涨家数占比 * 100 [10:90]
    #       c.(市场成交额 - 0.9万亿) / 1e10 [-40:40]

    @staticmethod
    def get_index_motion(a, b, c):
        result = int(((a + b + c) - (-110)) * 100 / (210 - (-110)))
        # logging.log(logging.DEBUG, "get_index_motion: " + str(result))
        return result

    # 获取指数涨跌幅
    # 注意，是 shang_zhen_zhi_shu 存储的是0.xx ，代表的是 0.xx% ，所以要先/100
    @staticmethod
    def get_a_index_zdf(shang_zhen_zhi_shu):
        result = shang_zhen_zhi_shu / 100 * 2000
        # logging.log(logging.DEBUG, "get_a_index_zdf: " + str(result))
        if result > 80:
            return 80
        elif result < -80:
            return -80
        else:
            return result

    # 获取上涨家数占比
    @staticmethod
    def get_b_rate_szjs(SZJS, XDJS, PPJS):
        result = SZJS / (SZJS + XDJS + PPJS) * 100
        # logging.log(logging.DEBUG, "get_b_rate_szjs: " + str(result))
        if result > 90:
            return 90
        elif result < 10:
            return 10
        else:
            return result

    # 获取市场成交额
    # total_trade_money: 单位是亿，因此需要x10e8,再/10e10 == /100
    @staticmethod
    def get_c_trade_money(total_trade_money):
        result = (total_trade_money - 9000) / 100
        # logging.log(logging.DEBUG, "get_c_trade_money: " + str(result))
        if result > 40:
            return 40
        elif result < -40:
            return -40
        else:
            return result

