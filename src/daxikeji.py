"""
@author: zkjiang
@contact: jiang_zhenkang@163.com
@software: PyCharm
@file: daxikeji.py
@time: 2018/12/27 19:11
"""


def find_max_length(sample_list):
    fill_seat_list = []
    # max_lengh = 0
    if not isinstance(sample_list, list):
        return None
    list_length = len(sample_list)
    if list_length < 1 or list_length > 20000:
        return None
    if len(sample_list) == 0:
        return 0
    for i in range(list_length):
        if sample_list[i] == 1:
            fill_seat_list.append(i)
    if len(fill_seat_list) == 0:
        return 0
    elif len(fill_seat_list) == 1:
        return max(fill_seat_list[0], list_length - fill_seat_list[0] - 1 )
    else:
        max_lengh = max(fill_seat_list[0], list_length - fill_seat_list[-1] - 1)
        for j in range(1,len(fill_seat_list)):
            max_lengh = max(max_lengh,int((fill_seat_list[j] - fill_seat_list[j - 1])/2))
        return max_lengh


if __name__ == '__main__':
    test_list = [1,0,1,0,1,1,0,1,0,0,1]
    print(find_max_length(test_list))