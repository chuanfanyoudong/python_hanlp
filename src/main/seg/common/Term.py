"""
@author: zkjiang
@contact: jiang_zhenkang@163.com
@software: PyCharm
@file: Term.py
@time: 2019/1/1 21:49
"""

"""
单词类，用户可以直接访问单词的全部属性
"""


class Term(object):

    def __init__(self, word, nature):
        self.word = word  # 词语
        self.nature = nature  # 词性

    def __str__(self):
        return self.word + "/" + self.nature

    def length(self):
        """
        :return:词的长度
        """
        return len(self.word)

    def getFrequency(self):
        """
        获取词语在python_hanlp词库的频次
        后续需要补充对词表的类
        :return: 频次， 0代表这是个新词
        """
        return 0

    def equals(self, obj):
        """
        比较两个Term是否相等
        :param obj: 0或者1
        :return:
        """
        if isinstance(obj, Term):
            if self.nature == obj.nature and self.word == obj.word:
                return 1
        return 0