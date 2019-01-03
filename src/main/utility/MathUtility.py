"""
@author: zkjiang
@contact: jiang_zhenkang@163.com
@software: PyCharm
@file: MathUtility.py
@time: 2019/1/2 21:24
"""
import math
from src.main.utility.Predefine import Predefine
MAX_FREQUENCY, dSmoothingPara, dTemp = Predefine.MAX_FREQUENCY, Predefine.dSmoothingPara, Predefine.dTemp

"""
一些数学工具类
"""

class MathUtility():



    def calculateWeight(self, from_way, to):
        """
        计算从一个词到另一个词的花费
        :param from_way: 前面的词
        :param to: 后面的词
        :return: 分数
        """
        frequency = from_way.getAttribute().toFrequency
        if frequency == 0:
            frequency = 1  # 防止发生除零错误
        nTwoWordsFreq = CoreBiGramTableDictionary.getBiFrequency(from_way.wordID, to.wordID)
        value = -math.log(dSmoothingPara * frequency/MAX_FREQUENCY + (1 - dSmoothingPara) * ((1 - dTemp) \
            * nTwoWordsFreq/frequency + dTemp))
        if value < 0:
            value = -value
        return value
