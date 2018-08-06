#!/usr/local/bin/python3
import sys
# input file handle reads csv lines output list of the list of values
def parse_csv(fh=sys.stdin):
    csv_items = []
    for line in fh:
        line = line.rstrip()
        csv_items.append(line.split(','))
    return csv_items