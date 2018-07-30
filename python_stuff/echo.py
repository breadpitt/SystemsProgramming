#!/usr/local/bin/python3

import sys
print("Control d ends user input not enter")
quit = 'quit\n'
for line in sys.stdin:
    if line == quit:
        break
    sys.stdout.write("%s" % line)
    sys.stderr.write("%s" % line)

#print(usr_in)