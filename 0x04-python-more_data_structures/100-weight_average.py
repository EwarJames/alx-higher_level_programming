#!/usr/bin/python3


def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return 0
    av = 0
    n = 0
    for i in my_list:
        av += (i[0] * i[1])
        n += i[1]
    return (av / n)
