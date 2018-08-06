#!/usr/local/bin/python3
import csv
import sys
def main():
    path = "pretend_data.csv"
    csv_items = []
    #fieldnames = ["Name", "Grade"]
    #wreter.writerow({'Name':item[0]' Grade:item[1]})
    with open(path,'r') as fh: 
        #data = csv.DictReader(fh)
        read_data = csv.reader(fh)
        #'|'.join(read_data)
        for row in read_data:
            csv_items.append(row)
            

    with open(path, "w") as fw:
        my_write = csv.writer(fw, delimiter="|")
        for item in fw:
            my_write.writerow(item)
            print(item)

        '''
        data = csv.DictReader(fh)
        #print(data.fieldnames)
        print(data.fieldnames)
        for row in data:
            for field in data.fieldnames:
                sys.stdout.write("{} : {}".format(field, row[field]))
                sys.stdout.write("\n")

        '''

if __name__ == main():
    main()

