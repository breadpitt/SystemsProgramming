#!/usr/local/bin/python3

from functools import reduce


class Shape:
    def __init__(self, num_sides, side_lengths=[]):
        self.num_sides = num_sides
        self.side_lengths = side_lengths

    def perimeter(self):
        return reduce(lambda x, y: x + y, self.side_lengths)

    #def area(self):
     #   pass # Placeholder for virtual area function

class Square(Shape):
    def __init__(self, side_length, num_sides=4):
        self.num_sides = num_sides
        self.side_lengths = [side_length] * 4
        self.side_length = side_length
        
    def area(self):   
        return self.side_length * self.side_length

    def print_shape_details(self):
        print("Shape has {} sides, length {}, perimeter is {}, area {}".format(self.num_sides, self.side_length, self.perimeter(), self.area()))


class Rectangle(Shape):
    def __init__(self, side_length, width_length, num_sides=4):
        self.num_sides = num_sides
        self.side_lengths = [side_length * 4]
        self.side_length = side_length
        self.width_length = width_length
        self.side_length_list = [side_length, side_length, width_length, width_length]
        
    def area(self):   
        return self.side_length * self.width_length

    def print_shape_details(self):
        print("Shape has {} sides, perimeter {}, area {}, side length list is {}".format(self.num_sides, self.perimeter(), self.area(), self.side_length_list))


sqlength = float(input("Enter length for the square: "))
sq = Square(sqlength)

sq.print_shape_details()

length, height = input("Enter length and width for the rectangle: ").split(" ")
length, height = float(length), float(height)
rect = Rectangle(length, height)

rect.print_shape_details()