"""
@author: zkjiang
@contact: jiang_zhenkang@163.com
@software: PyCharm
@file: python_hanlp.py
@time: 2019/1/3 23:50
"""

"""
常用接口工具类
"""

class Hanlp():

    def Config(self):
        """
        库的全局配置
        :return:
        """
        DEBUG = False
        CoreDictionaryPath = "data/dictionary/CoreNatureDictionary.txt"  # 核心词典路径
        BiGramDictionaryPath = "data/dictionary/CoreNatureDictionary.ngram.txt"  # 2元语法词典路径
        CoreStopWordDictionaryPath = "data/dictionary/stopwords.txt"  # 停用词词典路径
        CoreSynonymDictionaryDictionaryPath = "data/dictionary/synonym/CoreSynonym.txt"  # 同义词词典路径