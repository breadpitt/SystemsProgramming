#!/usr/local/bin/python3

class ShoppingBag:
    def __init__(self):
        self.items = {}

    def add_items(self, item, num):
        if item in self.items:
            self.total = int(self.items[item])
            self.total += num
            self.items[item] = self.total
        else: 
            self.items[item] = num
    def sub_items(self, item, num):
        if item in self.items:
            self.total = int(self.items[item])
            self.total -= num
            if self.total < 0:
                self.items[item] = 0
            else:
                self.items[item] = self.total
        else: 
            print("That item isn't in the bag")
    def __sub__(self, other):
        for i in self.items:
            if i in other.items:
                other.total = int(other.items[i])
                self.total = int(self.items[i])
                self.subbed = self.total - other.total
                if self.subbed < 0: # ok trying to get rid of these items 
                    self.subbed = other.total - self.total
                    if self.subbed < 0:
                        self.items[i] = 0
                    else:
                        self.items[i] = self.subbed
                else:
                    self.items[i] = self.subbed
            else:
                print("There already aren't any of those in the bag ")
        return self
    def __add__(self, other):
        for i in self.items:
            if i in other.items:
                other.total = int(other.items[i])
                self.total = int(self.items[i])
                other.summed = other.total + self.total
                other.items[i] = other.summed
            else:
                other.items[i] = self.items[i]
        return other
    
    def print_bag(self):
        for i in self.items:
            print("There are: {} {}s ".format(self.items[i], i))

my_bag = ShoppingBag()

my_bag.add_items('Apple', 10)
your_bag = ShoppingBag()
your_bag.add_items('banana', 10)
our_bag = my_bag + your_bag
our_bag = our_bag - your_bag
our_bag.print_bag()