import datetime

from chinese_calendar import is_workday, find_workday


class StockUtils:

    # 当前时间是否为A股的交易时间
    @staticmethod
    def a_stock_is_trade_time():
        if StockUtils.today_is_a_stock_trade_day():
            # A股交易时间范围
            n_date = datetime.datetime.now().date()
            morning_start_time = datetime.datetime.strptime(str(n_date) + '9:15', '%Y-%m-%d%H:%M')
            morning_end_time = datetime.datetime.strptime(str(n_date) + '11:30', '%Y-%m-%d%H:%M')
            afternoon_start_time = datetime.datetime.strptime(str(n_date) + '13:00', '%Y-%m-%d%H:%M')
            afternoon_end_time = datetime.datetime.strptime(str(n_date) + '15:00', '%Y-%m-%d%H:%M')
            # 当前时间
            n_time = datetime.datetime.now()
            # 判断当前时间是否在范围时间内
            is_in_trade_time = ((morning_end_time >= n_time >= morning_start_time) or
                                (afternoon_end_time >= n_time >= afternoon_start_time))
            return is_in_trade_time
        else:
            return False

    # 当前日期A股是交易日
    @staticmethod
    def today_is_a_stock_trade_day():
        # 当前时间
        n_time = datetime.datetime.now()
        # 当前是工作日（注意：周末可能因为调休的原因也可能是工作日）
        current_is_work_day = is_workday(n_time)
        # 返回今天星期几（0代表周一）
        week_day = n_time.weekday()
        # 工作日、且为周一到周五
        return current_is_work_day and week_day < 5

    @staticmethod
    def get_previous_work_day():
        """获取前面的工作日"""
        previous_day = find_workday(-1)
        return previous_day

    # 仅用于判定当前时间是13点之前还是之后
    @staticmethod
    def time_is_before_13_clock():
        # A股交易时间范围
        n_date = datetime.datetime.now().date()
        time_13 = datetime.datetime.strptime(str(n_date) + '13:00', '%Y-%m-%d%H:%M')
        # 当前时间
        n_time = datetime.datetime.now()
        return n_time < time_13

    # 仅用于判定当前时间是15点之前还是之后
    @staticmethod
    def time_is_after_15_clock():
        # A股交易时间范围
        n_date = datetime.datetime.now().date()
        time_13 = datetime.datetime.strptime(str(n_date) + '15:00', '%Y-%m-%d%H:%M')
        # 当前时间
        n_time = datetime.datetime.now()
        return n_time >= time_13

    # 仅用于判定当前时间是在9:15开盘之前还是之后
    @staticmethod
    def time_is_after_trade():
        # A股交易时间范围
        n_date = datetime.datetime.now().date()
        time_start_trade = datetime.datetime.strptime(str(n_date) + '9:15', '%Y-%m-%d%H:%M')
        # 当前时间
        n_time = datetime.datetime.now()
        return n_time >= time_start_trade

    # 获取最近的交易日的日期，如果今天是交易日就返回今天
    @staticmethod
    def get_most_recent_trade_day():
        if StockUtils.today_is_a_stock_trade_day():
            return datetime.datetime.now().strftime('%Y-%m-%d')
        else:
            # 最近的一个工作日
            previous_work_day = StockUtils.get_previous_work_day()
            # 返回星期几（数字0 代表周一）
            week_day = previous_work_day.weekday()
            if week_day < 5:  # 小于5 代表是周一到周五的工作日
                return previous_work_day.strftime('%Y-%m-%d')
            else:  # 周六周日，应该返回周六周日之前的最近一个周一到周五的工作日
                # todo 找到周五，待处理
                return 0

    # 获取最近的num个交易日的日期，如果今天是交易日就包括今天
    @staticmethod
    def get_most_num_trade_day(num):
        if_trade_time = StockUtils.today_is_a_stock_trade_day() & StockUtils.time_is_after_trade()
        if if_trade_time:
            end_day = datetime.datetime.now().strftime('%Y-%m-%d')
            end_time = datetime.datetime.strptime(str(end_day) + '15:00', '%Y-%m-%d%H:%M')

            """获取前面的工作日"""
            previous_day = find_workday(-num)
            start_time = datetime.datetime.strptime(str(previous_day) + '9:15', '%Y-%m-%d%H:%M')

        else:
            end_day = find_workday(-1)
            end_time = datetime.datetime.strptime(str(end_day) + '15:00', '%Y-%m-%d%H:%M')

            """获取前面的工作日"""
            previous_day = find_workday(-(num+1))
            start_time = datetime.datetime.strptime(str(previous_day) + '9:15', '%Y-%m-%d%H:%M')

        json_data = {'start_time': start_time, 'end_time': end_time}
        return json_data




