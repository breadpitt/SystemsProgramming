#!/usr/local/bin/python3

while True:
    usr_input = input("enter input: ")
    try:
        int(usr_input)
        break
    except ValueError as err:
        print("that's a string")
        print("Full error was %s " % (str(err)))
    except Exception as err:
        print("Some other exception occured. Type was %s and full error is %s " % (type(err), str(err)))
        