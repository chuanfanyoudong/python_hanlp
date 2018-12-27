"""
@author: zkjiang
@contact: jiang_zhenkang@163.com
@software: PyCharm
@file: Edge.py
@time: 2018/12/27 22:13
"""

"""
基础的类-边
"""

class Edge(object):

    def __init__(self, weight, name):
        """
        该类具有权重和名字两个属性
        :param weight:
        :param name:
        """
        self.weight = weight
        self.name = name



