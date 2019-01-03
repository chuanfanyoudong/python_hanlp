"""
@author: zkjiang
@contact: jiang_zhenkang@163.com
@software: PyCharm
@file: CoreBiGramTableDictionary.py
@time: 2019/1/3 23:16
"""

"""
核心词典的二元词典
"""

class CoreBiGramTableDictionary():

    def __init__(self):
        self.pair = []  # pair[偶数n]表示key，pair[n+1]表示frequency
        self.start = []

    def getBiFrequency(self, idA, idB):
        """
        获取共现频率
        :param idA: 第一个词的id
        :param idB: 第二个词的id
        :return: 共现频次
        """
        if idA < 0:  # 负数表示来自用户词典的词语的词频，因为用户自定义词语没有id，返回正值增加亲和度
            return -idA
        if idB < 0:
            return -idB



