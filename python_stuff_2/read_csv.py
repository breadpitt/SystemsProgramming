#!/usr/local/bin/python3
import mycsv

def main():
    # works but should use with
    path = "pretend_data.csv"

    with open(path, 'r') as fh:
        data = mycsv.parse_csv(fh)
        for i in data:
            print("Name {} has grade {}".format(i[0], i[1]))
if __name__ == main():
    main()
