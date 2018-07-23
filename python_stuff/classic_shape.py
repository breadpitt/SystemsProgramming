#!/usr/local/bin/python3

from functools import reduce


class Shape:
    def __init__(self, num_sides, side_lengths=[]):
        self.num_sides = num_sides
        self.side_lengths = side_lengths

    def perimeter(self):
        return reduce(lambda x, y: x + y, self.side_lengths)

    def area(self):
        pass # Placeholder for virtual area function

class Square(Shape):
    def __init__(self, side_length, num_sides=4):
        self.num_sides = num_sides
        self.side_lengths = [side_length] * 4
        
    def area(self):   
        return self.side_lengths * self.side_lengths

    def print_shape_details(self):
        print("Shape has %d sides, perimeter %f, area %f" % (self.num_sides, self.perimeter(), self.area()))


class Rectangle(Shape):
    def __init__(self, side_length, side_width):
        self.num_sides = num_sides
        self.side_length = side_length
        self.side_width = side_width
        self.side_length_list = [side_length, side_length, side_width, side_width]
        
    def area(self):   
        return self.side_lengths * self.side_width

    def print_shape_details(self):
        print("Shape has {} sides, perimeter {}, area {}".format(self.side_lengths, self.perimeter(), self.area(), self.side_length_list))