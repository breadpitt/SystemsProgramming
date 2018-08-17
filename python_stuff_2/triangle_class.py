#!/usr/local/bin/python3
import math
class triangle:
    def __init__(self, lenone, lentwo, base):
        self.lenone = float(lenone)
        self.lentwo = float(lentwo)
        self.base = float(base)
        self.hght = 0
        self.a = 0
        self.x = 0
        self.y = 0
        self.z = 0
        if lenone + lentwo < base:
            print("Error")
            exit

    def perimeter(self):
        self.p = self.base + self.lenone + self.lentwo
        return self.p
    

    def height(self, lenone, base):
            self.b = (self.lenone*self.lenone) - (self.base*self.base)
            print(self.b)
            self.hght = math.sqrt(self.b)
            return self.hght
            #return self.h
        

    def area(self):
        self.a = math.sqrt(self.lentwo*(self.lentwo - self.base)*(self.lentwo - self.hght)*(self.lentwo - self.lenone))
        

    def print_details(self):
        self.x = self.perimeter()
        self.y = self.height(self.lenone, self.base)
        self.z = self.area()
        print("Perimeter = {} Height = {} Area = {}".format(self.x, self.y, self.z))

my_triangle = triangle(10, 10, 10)
my_triangle.print_details()