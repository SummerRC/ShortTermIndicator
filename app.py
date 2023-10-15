import os
import logging

from flask import (
    Flask, url_for, render_template
)

from DBUtils import DBUtils


app = Flask(__name__)


@app.route('/')
def index():
    return echarts()


@app.route('/echarts')
def echarts():
    db_util = DBUtils()
    # 查询最近40个交易日的综合强度数据
    db_util.query_zhqd_timestamps_from_db()
    timestamps = db_util.get_timestamps()
    zhqds = db_util.get_zhqds()

    # 查询最近一个交易日当天的综合强度数据
    db_util.query_most_recent_trade_day_zhqds_from_db()
    most_recent_day_zhqds = db_util.get_most_recent_day_zhqds()
    most_recent_day_timestamps = db_util.get_most_recent_day_timestamps()

    # 查询连板高度和对应的交易日
    db_util.query_highest_from_db()
    trade_day = db_util.get_trade_day()
    highest = db_util.get_highest()

    return render_template('echarts.html', timestamps=timestamps, zhqds=zhqds,
                           most_recent_day_zhqds=most_recent_day_zhqds,
                           most_recent_day_timestamps=most_recent_day_timestamps,
                           trade_day=trade_day, highest=highest)


def get_absolute_file_path(filename):
    basedir = os.path.abspath(os.path.dirname(__file__))
    absolute_file_path = basedir + url_for('static', filename='img/' + filename)
    return absolute_file_path


# 使用 errorhandler() 装饰器定制出错页面
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    app.run()

