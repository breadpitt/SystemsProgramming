#!/usr/local/bin/python3
import mycsv
path = "pretend_data.csv"
fh = open(path,'r')
def main(): 
    data = mycsv.parse_csv(fh)
    for i in data:
        print("Name {} has grade {}".format(i[0], i[1]))
if __name__ == main():
    main()
