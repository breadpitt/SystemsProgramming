#!/usr/local/bin/python3

inlist = [5, 8, 9, 4, 3]
def rang(inpt):
    tmplist = []
    for i in range(inpt, -1, -1):
        tmplist.append(i)
    return tmplist
outlist = list(map(lambda x: rang(x), inlist))

for i in outlist:
    print(i)