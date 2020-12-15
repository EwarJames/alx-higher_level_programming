#!/usr/bin/python3


def element_at(my_list, idx):
    for idx in range(len(my_list)):
        if idx < 0 and idx > range(len(my_list)):
            return None
        else:
            return len(my_list) - 1
