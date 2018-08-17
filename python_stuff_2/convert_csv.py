#!/usr/local/bin/python3
import csv
import sys
def main():
    path = "pretend_data.csv"
    write_path = "pretend_csv.txt"
    csv_items = []
    csv_dict = {}
    #fieldnames = ["Name", "Grade"]
    #wreter.writerow({'Name':item[0]' Grade:item[1]})
    with open(path,'r') as fh: 
        #data = csv.DictReader(fh)
        read_data = csv.reader(fh)
        #'|'.join(read_data)
        for row in read_data:
            csv_items.append(row)
            for i in row:
                csv_dict[row[0]] = row[1]
        with open(write_path, "w") as fw:
            fieldnames = ['Name', 'Grade']
            my_write = csv.DictWriter(fw, fieldnames=fieldnames, delimiter="|")
            my_write.writeheader()
            my_write.writerow(csv_dict)
            #for row in csv_dict:
             #   my_write.writerow(row)
                #  print(row)
    print(csv_dict)
    '''

    with open('names.csv', newline='') as csvfile:
...     reader = csv.DictReader(csvfile)
...     for row in reader:
...         print(row['first_name'], row['last_name'])
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

