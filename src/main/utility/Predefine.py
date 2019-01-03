"""
@author: zkjiang
@contact: jiang_zhenkang@163.com
@software: PyCharm
@file: Predefine.py
@time: 2019/1/2 21:37
"""

"""
定义一些全局变量
"""


class Predefine():


    CHINESE_NUMBERS = "零○〇一二两三四五六七八九十廿百千万亿壹贰叁肆伍陆柒捌玖拾佰仟"
    """
    hanlp.properties的路径
    """
    HANLP_PROPERTIES_PATH = ""
    MIN_PROBABILITY = 1e-10
    """
    总词频
    """
    MAX_FREQUENCY = 25146057
    """
    平滑因子
    """
    dSmoothingPara = 0.1
    """
    Smothing 平滑因子
    """
    dTemp = 1 / MAX_FREQUENCY + 0.00001

if __name__ == '__main__':
    print(Predefine.MAX_FREQUENCY)