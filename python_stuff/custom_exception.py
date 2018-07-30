#!/usr/local/bin/python3


class FileNotFound(Exception):
    def __init__(self):
        pass

class DogAteHomework(Exception):
    def __init__(self, description):
        self.description = description


while True:
    usr_input = input("enter a number greater than 5: ")
    try:
        int(usr_input)
        usr_input = int(usr_input)
        if usr_input > 5:
            break
        elif usr_input < 5:
            raise FileNotFoundError
        elif usr_input == 5:
            raise DogAteHomework("bad dog")
        
    except FileNotFoundError:
        print("file not found also that's less than 5")
    except DogAteHomework as e:
        print('Dog ate homework ', e.description)
        