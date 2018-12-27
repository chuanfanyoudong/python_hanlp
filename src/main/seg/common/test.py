"""
@author: zkjiang
@contact: jiang_zhenkang@163.com
@software: PyCharm
@file: test.py
@time: 2018/12/27 22:34
"""


class A(object):
    def __init__(self, xing, gender):
        self.namea = "aaa"
        self.xing = xing
        self.gender = gender

    def funca(self):
        print
        "function a : %s" % self.namea


class B(A):
    def __init__(self, xing, gender, age):
        # super(B, self).__init__(xing, age)
        self.nameb = "bbb"
        ##self.namea="ccc"
        self.xing = xing.upper()
        self.age = age + 1
        # self.gender = gender.upper()

    def funcb(self):
        print("function b : %s" % self.nameb)


b = B("lin", "nan", 22)
print(b.nameb)
# print(b.namea)
b.funcb()
# b.funca()
# print
# b.gender  #####