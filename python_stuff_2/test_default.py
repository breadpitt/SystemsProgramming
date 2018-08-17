#!/usr/local/bin/python3

def optional_args(first = "Hello", second = "Guest"):
    return first, second

print(optional_args())
print(optional_args(second = "Will"))