#!/usr/local/bin/python3


def concatenate_strings(first, second):
    retval = ""
    if first != None and second != None:
        retval = "%s%s" % (first, second)
    return retval

def test():
    checkval = "Hello World"
    ret = concatenate_strings("Hello ", "World")
    if ret == checkval:
        print("Cat works!")
    else:
        print("Cat is broken")
# Defines a main function
#def main():
 ##  test()

# Check if name == to main

#if __name__ == "__main__":
    # if yes call main
 #   main()

#else:
 #   print("Python script has been included in another program")
