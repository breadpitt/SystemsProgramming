#!/usr/local/bin/python3

mylist = [10,23,66,4,87,200,0]
def top_two(list):
    a = len(list)
    if a < 2:
        print("Error provided list too small")
    max = list[0]
    secmax = list[1]
    
    if max < secmax:
        temp = max
        max = secmax
        secmax = temp

    for i in list:
        if max < i:
            secmax = max
            max = i

    return max, secmax 
            



first , second = top_two(mylist)

print("The two highest numbers from the list are %d and %d " % (first , second))