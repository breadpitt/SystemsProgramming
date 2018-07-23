#!/usr/local/bin/python3

from functools import reduce







def input_list(inpt):
    total = 0 
    for x in input_list:
        if total == 0:
            total = x
        else:
            total = total * x

    return total

lurst = [5, 4, 3, 2]

exlist = list(map(lambda x: input_list(lurst), lurst))

print(exlist)