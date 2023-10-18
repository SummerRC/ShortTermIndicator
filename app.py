import os
import logging

from flask import (
    Flask, url_for, render_template, Response, request
)

from utils.config_helper import ConfigHelper
from utils.echart_data_helper import EchartsDataHelper

app = Flask(__name__)


@app.before_request
def require_login():
    config_helper = ConfigHelper()
    if config_helper.need_login:
        auth = request.authorization
        if not auth:
            return authenticate()

        login_suc = ((auth.username == config_helper.user_name and auth.password == config_helper.password) or
                     (auth.username == config_helper.temp_user and auth.password == config_helper.temp_user_password))
        if not login_suc:
            return authenticate()


@app.route('/')
def index():
    data_helper = EchartsDataHelper()
    return render_template('echarts_less_data.html', json=data_helper.get_echarts_json_data(False))


@app.route('/echarts')
def echarts():
    data_helper = EchartsDataHelper()
    return render_template('echarts_more_data.html', json=data_helper.get_echarts_json_data(True))


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

# http://flask.pocoo.org/snippets/category/authentication/
def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response("<script>alert('Fail to login: basic auth for ScrapydWeb has been enabled');</script>",
                    401, {'WWW-Authenticate': 'Basic realm="ScrapydWeb Basic Auth Required"'})