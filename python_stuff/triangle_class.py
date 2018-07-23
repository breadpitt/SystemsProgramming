#!/usr/local/bin/python3
import math
class triangle:
    def __init__(self, lone, base):
        self.lone = float(lone)
        self.base = float(base)

        if lone < base:
            print("Error")
            exit

    def perimeter(self):
        p = self.base + self.lone + self.lone
        return p
        #print("Perimeter is: %d " % p)

    def height(self):
            b = (self.lone*self.lone) - (self.base*self.base)
            h = math.sqrt(b)
            return h
            #print("Height is: %d " % h)
        

    def area(self):
        ptwo = self.perimeter / 2
        hght = self.height
        a = math.sqrt(ptwo*(ptwo - base)*(ptwo - hght)*(ptwo - lone))
        return a

    def print_details(self):
        x = self.perimeter()
        y = self.height()
        z = self.area()
        print("Perimeter = %f Height = %f Area = %f" % x, y, z)

my_triangle = triangle(5, 10)

my_triangle.print_details()