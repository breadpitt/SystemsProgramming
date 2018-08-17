#!/usr/local/bin/python3

from functools import reduce


class Shape:
    def __init__(self, num_sides, side_lengths=[]):
        self.num_sides = num_sides
        self.side_lengths = side_lengths
        
    def perimeter(self, self_lengths):
        self.perim = sum(self_lengths)
        return self.perim
    def area(self):
        return reduce(lambda x, y: x * y, self.side_lengths)

   # def area(self):
    #    pass # Placeholder for virtual area function

class Rectangle(Shape):
        def __init__(self, num_sides, side_lengths=[]):
            super().__init__(num_sides, side_lengths)
            self.num_sides = num_sides
            self.side_lengths = side_lengths

class Square(Rectangle):
    def __init__(self, side_lengths=[]):
        super().__init__(side_lengths)
        self.num_sides = 4
        self.side_lengths = [side_lengths] * 4
        self.perime = self.perim(side_lengths)
    def print_shape_details(self):
        print("Square has a perimeter of: {}".format(self.perime))
        
            
f = [5, 5]
s = Square(f)

sides = [4, 4]
v = Rectangle(4, sides)

s.print_shape_details()