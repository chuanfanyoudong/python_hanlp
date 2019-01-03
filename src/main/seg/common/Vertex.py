"""
@author: zkjiang
@contact: jiang_zhenkang@163.com
@software: PyCharm
@file: Vertex.py
@time: 2019/1/1 22:17
"""

"""
顶点类
"""

class Vertex():

    def __init__(self, word, ):
        self.word = word  # 顶点这个词

    def updateFrom(self, from_way):
        weight = from_way.weight +