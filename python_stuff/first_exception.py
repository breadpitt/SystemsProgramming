#!/usr/local/bin/python3

while True:
    usr_input = input("enter input: ")
    try:
        int(usr_input)
        break
    except ValueError:
        print("that's a string")
    # finally:
        # code get's run no matter what happens
        