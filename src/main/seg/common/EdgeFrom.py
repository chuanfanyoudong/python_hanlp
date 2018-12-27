"""
@author: zkjiang
@contact: jiang_zhenkang@163.com
@software: PyCharm
@file: EdgeFrom.py
@time: 2018/12/27 22:17
"""

from src.main.seg.common.Edge import Edge

"""
定义了起点的边
"""


class EdgeFrom(Edge):

    def __init__(self, weight, name, from_way):
        """
        继承了Edge这个类，然后加上了from_way这个参数
        :param weight:
        :param name:
        :param from_way:
        """
        super(EdgeFrom, self).__init__(weight, name)
        self.from_way = from_way

    def __str__(self):
        """
        重写了__str__方法
        :return:
        """
        return "EdgeFrom{" + "from_way = " + str(self.from_way) + ", weight = " + str(self.weight) + ", name='" + str(self.name) + "\'" + "}"



# df = EdgeFrom(1,2,3)
# print(df.__str__())