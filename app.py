import os
import logging

import numpy as np
from flask import (
    Flask, request, url_for, render_template
)

from DBUtils import DBUtils
from MatplotUtils import MatplotUtils


app = Flask(__name__)


@app.route('/')
def index():
    db_util = DBUtils()
    db_util.query_zhqd_timestamps_from_db()
    timestamps = np.array(db_util.get_timestamps())
    zhqds = np.array(db_util.get_zhqds())

    return render_template('index.html', timestamps=timestamps, zhqds=zhqds)


@app.route('/echarts')
def echarts():
    db_util = DBUtils()
    # 查询最近40个交易日的综合强度数据
    db_util.query_zhqd_timestamps_from_db()
    timestamps = np.array(db_util.get_timestamps())
    zhqds = np.array(db_util.get_zhqds())

    # 查询最近一个交易日当天的综合强度数据
    db_util.query_most_recent_trade_day_zhqds_from_db()
    most_recent_day_zhqds = db_util.get_most_recent_day_zhqds()
    most_recent_day_timestamps = db_util.get_most_recent_day_timestamps()

    return render_template('echarts.html', timestamps=timestamps, zhqds=zhqds,
                           most_recent_day_zhqds=most_recent_day_zhqds,
                           most_recent_day_timestamps=most_recent_day_timestamps)


@app.route('/cyberpunk')
def cyberpunk_plot_pic():
    filename = "tmp_cyberpunk.png"
    db_util = DBUtils()
    db_util.query_zhqd_timestamps_from_db()
    matplot_util = MatplotUtils()
    matplot_util.init_y_data(db_util.get_zhqds(), db_util.get_timestamps())
    matplot_util.save_cyberpunk_plot_pic(get_absolute_file_path(filename))
    # 传递图形路径给模板
    return render_template('matplotx.html', filename=filename)


@app.route('/matplotx_light')
def matplotx_light_pic():
    filename = "tmp_matplotx_light.png"
    db_util = DBUtils()
    db_util.query_zhqd_timestamps_from_db()
    matplot_util = MatplotUtils()
    matplot_util.init_y_data(db_util.get_zhqds(), db_util.get_timestamps())
    matplot_util.save_matplotx_light_pic(get_absolute_file_path(filename))
    # 传递图形路径给模板
    return render_template('matplotx.html', filename=filename)


@app.route('/matplotx_dark')
def matplotx_dark_pic():
    filename = "matplotx_dark.png"
    db_util = DBUtils()
    db_util.query_zhqd_timestamps_from_db()
    matplot_util = MatplotUtils()
    matplot_util.init_y_data(db_util.get_zhqds(), db_util.get_timestamps())
    matplot_util.save_matplotx_dark_pic(get_absolute_file_path(filename))
    # 传递图形路径给模板
    return render_template('matplotx.html', filename=filename)


@app.route('/quantum_black')
def quantum_black_pic():
    filename = "quantum_black.png"
    db_util = DBUtils()
    db_util.query_zhqd_timestamps_from_db()
    matplot_util = MatplotUtils()
    matplot_util.init_y_data(db_util.get_zhqds(), db_util.get_timestamps())
    matplot_util.save_quantum_black_pic(get_absolute_file_path(filename))
    # 传递图形路径给模板
    return render_template('matplotx.html', filename=filename)


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

