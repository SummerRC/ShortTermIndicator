import matplotx
import mplcyberpunk
import numpy as np
from matplotlib import pyplot as plt
from qbstyles import mpl_style

# 使用matplotlib下的font_manager
from matplotlib import font_manager

import matplotlib
matplotlib.use('Agg')


class MatplotUtils:

    y_data = []
    y_text = []

    # 实例化 font_manager
    chinese_font = font_manager.FontProperties(family='Songti SC', size=12)

    def __init__(self):
        pass

    # 保存赛博朋克样式折线图
    def save_cyberpunk_plot_pic(self, absolute_file_path):
        # 使用赛博朋克风样式并设置发光效果
        plt.style.use('cyberpunk')
        mplcyberpunk.make_lines_glow()

        self.common_setting()

        # 保存图形到临时文件
        plt.savefig(absolute_file_path)
        # 清除图形
        plt.clf()

    # 保存matplotx优化的折线图
    def save_matplotx_light_pic(self, absolute_file_path):
        with plt.style.context(matplotx.styles.pitaya_smoothie['light']):
            self.common_setting()

            # 保存图形到临时文件
            plt.savefig(absolute_file_path)
            # 清除图形
            plt.clf()

    # 保存matplotx优化的折线图
    def save_matplotx_dark_pic(self, absolute_file_path):
        with plt.style.context(matplotx.styles.pitaya_smoothie['dark']):
            self.common_setting()

            # 保存图形到临时文件
            plt.savefig(absolute_file_path)
            # 清除图形
            plt.clf()

    # 保存QuantumBlack优化的折线图
    def save_quantum_black_pic(self, absolute_file_path):
        # 深色主题
        mpl_style(dark=True)

        self.common_setting()

        # 保存图形到临时文件
        plt.savefig(absolute_file_path)
        # 清除图形
        plt.clf()

    def common_setting(self):
        # x、y轴尺寸
        plt.figure(figsize=(8, 6.6))
        # 折线图
        plt.plot(self.y_data, marker='o')

        # Y轴范围
        plt.ylim((0, 100))
        # Y轴刻度
        y_ticks = np.array([0, 25, 50, 75, 100])
        plt.yticks(y_ticks)
        # 坐标轴名称
        plt.xlabel('日期', fontproperties=self.chinese_font)
        plt.ylabel('情绪强度', fontproperties=self.chinese_font)
        # 设置右边和上边无边框
        ax = plt.gca()
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')

    def init_y_data(self, y, text):
        self.y_data = np.array(y)
        self.y_text = text





