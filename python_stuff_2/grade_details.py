#!/usr/local/bin/python3
path = "pretend_data.csv"
import sys
num, total, count, avg = 0, 0, 0, 0
numlist = []
with open(path, 'r') as csv:
    for line in csv:
        line = line.strip(' ')
        lurst = line.split(',')
        num = int(lurst[1])
        numlist.append(num)
        total += num
        count += 1
        #sys.stdout.write(format(str(num))
        print("%s" % str(num))
print(total)
avg = float(total) / count
print(avg)
print(max(numlist))
print(min(numlist))

