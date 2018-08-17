#!/usr/local/bin/python3
path = "alice.txt"
user_path = input("Type file name ")
try:
    fr = open(path, 'r')
except FileNotFoundError:
    print("FNF")
try:
    out_file = "%s.copy" % (path)
    fo = open(out_file, 'w')
except FileExistsError:
    print("FNF")

line = fr.readline()
while line:
    fo.write(line)
    line = fr.readline()

fr.close()
fo.close()
try:
    fa = open(user_path, 'r')
except FileNotFoundError:
    print("FNF")
try:
    out_file = "%s.copy" % (user_path)
    fb = open(out_file, 'w')
except FileExistsError:
    print("FNF")
line = fa.readline()
while line:
    fb.write(line)
    line = fa.readline()

fa.close()
fb.close()