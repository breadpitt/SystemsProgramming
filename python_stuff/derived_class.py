#!/usr/local/bin/python3

from functools import reduce


class Shape:
    def __init__(self, num_sides, side_lengths=[]):
        self.num_sides = num_sides
        self.side_lengths = side_lengths

    def perimeter(self):
        return reduce(lambda x, y: x + y, self.side_lengths)

    def area(self):

        return reduce(lambda x, y: x * y, self.side_lengths)

    def area(self):
        pass # Placeholder for virtual area function

class Rectangle(Shape):
        def __init__(self, num_sides, side_lengths=[]):
                super(Rectangle, self).__init__()
                self.num_sides = num_sides
                self.side_lengths = side_lengths
                print(self.lsit)

class Square(Rectangle):
    def __init__(self, side_length, num_sides=4):
        self.num_sides = num_sides
        self.side_lengths = [side_length] * 4
        super(Square, self).__init__()
        print(self.mylist)
    def print_shape_details(self):
        print("Shape has %d sides, perimeter %f, area %f" % (self.num_sides, self.perimeter(), self.area()))