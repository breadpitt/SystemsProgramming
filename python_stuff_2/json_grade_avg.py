#!/usr/local/bin/python3
import json
json_string = ""
#input_data = ""
# grade_obj["students"][0]["grades"][0]["assn1"] gets the value for assn1 for first student in grades
num, total, avg, count = 0,0,0,0
with open('grades.json') as json_fh:
    input_data = json.load(json_fh)
    print(json.dumps(input_data))
    for i in input_data["students"]:
        for j in [i]:
            print("j %s " % j)
            for k in j["grades"]:
                print("k %s " % k)
                for v in k:
                    print("{}: {}".format(v, k[v]))
                    total += int(k[v])
                    count += 1
                avg = float(total) / count
                print("Average: %d" % avg)


                


           
        
                
