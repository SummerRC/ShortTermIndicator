import os
import logging

from flask import (
    Flask, url_for, render_template
)

from DBUtils import DBUtils
from utils.echart_data_helper import EchartsDataHelper

app = Flask(__name__)


@app.route('/')
def index():
    return echarts()


@app.route('/echarts')
def echarts():
    data_helper = EchartsDataHelper()
    return render_template('echarts.html', json=data_helper.get_echarts_json_data())


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

