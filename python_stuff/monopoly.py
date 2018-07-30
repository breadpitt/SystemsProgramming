#!/usr/local/bin/python3


# Initialize game

num_players = int(input("How many human players will be playing? "))

while num_players < 1 or num_players > 4:
    print("Number of players error. Please enter a number between 1 and 4")
    num_players = int(input("How many human players will be playing? "))

player_name = input("Please enter a name: ")

tokens = ['iron', 'doggie', 'top hat', 'cannon', 'wheelbarrow', 'battleship', 'thimble', 'race car', 'shoe']

player_token = input("Please choose a token from the list %s " % tokens)

while True:
    if player_token in tokens:
        tokens.remove(player_token) 
        print("%s" % tokens)
        break
    else:
        player_token = input("Player token error. Please choose a token still available from the list %s " % tokens)
        

class Player:
    properties = []
    position = ''
    money = 1500
    computer = True

    def __init__(self, name, token):
        self.name = name   
        self.token = token
        