#!/usr/local/bin/python3

import random

class GenErr(Exception):  # Generic error
            def __init(self):
                pass


class GameBoard:
    def __init__(self):
        self.tiles = [
            {'name': 'Go', 'cost': 0, 'location': 0,
                'type': 'pass', 'base_rent': 2, 'group': None},
            {'name': 'Mediterranean Avenue', 'cost': 60, 'location': 1,
                'type': 'property', 'base_rent': 2, 'group': 'brown', 'owner': None},
            {'name': 'Community Chest', 'cost': 0, 'location': 2, 'type': 'chest', 'base_rent': 0,
             'group': 'chill'},
            {'name': 'Baltic Avenue', 'cost': 60, 'location': 3,
                'type': 'property', 'base_rent': 4, 'group': 'brown', 'owner': None},
            {'name': 'Income Tax', 'cost': 0, 'location': 4, 'type': 'chest', 'base_rent': 100,
             'group': 'chill'},
            {'name': 'Reading RR', 'cost': 200, 'location': 5, 'type': 'railroad',
                'base_rent': '25', 'group': 'white', 'owner': None},
            {'name': 'Oriental Avenue', 'cost': '100', 'location': 6,
                'type': 'property', 'base_rent': '6', 'group': 'blue', 'owner': None},
            {'name': 'Chance', 'cost': 0, 'location': 7, 'type': 'chance', 'base_rent': 0,
             'group': 'chill'},
            {'name': 'Vermont Avenue', 'cost': '100', 'location': 8,
                'type': 'property', 'base_rent': '6', 'group': 'blue', 'owner': None},
            {'name': 'Connecticut Avenue', 'cost': '120', 'location': 9,
                'type': 'property', 'base_rent': '8', 'group': 'blue', 'owner': None},
            {'name': 'Jail', 'cost': 0, 'location': 10, 'type': 'chest', 'base_rent': 0,
             'group': 'chill'},
            {'name': 'St. Charles', 'cost': '140', 'location': 11, 'type': 'property',
                'base_rent': '10', 'group': 'purple', 'owner': None},
            {'name': 'Electric Company', 'cost': '150', 'location': 12,
                'type': 'utility', 'base_rent': '1', 'group': 'utility', 'owner': None},
            {'name': 'States Avenue', 'cost': '70', 'location': 13,
                'type': 'property', 'base_rent': '10', 'group': 'purple', 'owner': None},
            {'name': 'Virginia Avenue', 'cost': '160', 'location': 14,
                'type': 'property', 'base_rent': '12', 'group': 'purple', 'owner': None},
            {'name': 'Pennsylvania RR', 'cost': '200', 'location': 15, 'type': 'railroad',
                'base_rent': '25', 'base_rent': '25', 'group': 'white', 'owner': None},
            {'name': 'St. James', 'cost': 180, 'location': 16, 'type': 'property',
                'base_rent': '14', 'group': 'orange', 'owner': None},
            {'name': 'Community Chest', 'cost': 0, 'location': 17, 'type': 'chest', 'base_rent': 0,
             'group': 'chill'},
            {'name': 'Tennessee Avenue', 'cost': '180', 'location': 18,
                'type': 'property', 'base_rent': '14', 'group': 'orange', 'owner': None},
            {'name': 'New York', 'cost': 200, 'location': 19, 'type': 'property',
                'base_rent': '16', 'group': 'orange', 'owner': None},
            {'name': 'Free Parking', 'cost': 0, 'location': 20, 'type': 'parking', 'base_rent': 0,
             'group': 'chill'},
            {'name': 'Kentucky Avenue', 'cost': '220', 'location': 21,
                'type': 'property', 'base_rent': '18', 'group': 'red', 'owner': None},
            {'name': 'Chance', 'cost': 0, 'location': 22, 'type': 'chance', 'base_rent': 0,
             'group': 'chill'},
            {'name': 'Indiana Avenue', 'cost': '220', 'location': 23,
                'type': 'property', 'base_rent': '18', 'group': 'red', 'owner': None},
            {'name': 'Illinois Avenue', 'cost': '240', 'location': 24,
                'type': 'property', 'base_rent': '20', 'group': 'red', 'owner': None},
            {'name': 'B&O RR', 'cost': 200, 'location': 25, 'type': 'property',
                'base_rent': '25', 'group': 'white', 'owner': None},
            {'name': 'Atlantic Avenue', 'cost': '260', 'location': 26,
                'type': 'property', 'base_rent': '22', 'group': 'yellow', 'owner': None},
            {'name': 'Ventnor Avenue', 'cost': '260', 'location': 27,
                'type': 'property', 'base_rent': '22', 'group': 'yellow', 'owner': None},
            {'name': 'Water Works', 'cost': '150', 'location': 28, 'type': 'property',
                'base_rent': '1', 'group': 'utility', 'owner': None},
            {'name': 'Marvin Gardens', 'cost': 280, 'location': 29,
                'type': 'property', 'base_rent': '24', 'group': 'yellow', 'owner': None},
            {'name': 'Go To Jail!', 'cost': 0, 'location': 30, 'type': 'gotojail', 'base_rent': 0,
             'group': 'jail'},
            {'name': 'Pacific Avenue', 'cost': '300', 'location': 31,
                'type': 'property', 'base_rent': '26', 'group': 'green', 'owner': None},
            {'name': 'North Carolina', 'cost': 300, 'location': 32,
                'type': 'property', 'base_rent': '150', 'group': 'green', 'owner': None},
            {'name': 'Community Chest', 'cost': 0, 'location': 33, 'type': 'chest', 'base_rent': 0,
             'group': 'chill'},
            {'name': 'Pennsylvania Avenue', 'cost': '320', 'location': 34,
                'type': 'property', 'base_rent': '28', 'group': 'green', 'owner': None},
            {'name': 'Short Line', 'cost': 200, 'location': 35, 'type': 'property',
                'base_rent': '25', 'group': 'white', 'owner': None},
            {'name': 'Chance', 'cost': 0, 'location': 36, 'type': 'chance', 'base_rent': 0,
             'group': 'chill'},
            {'name': 'Park Place', 'cost': '350', 'location': 37, 'type': 'property',
                'base_rent': '35', 'group': 'darkblue', 'owner': None},
            {'name': 'Luxury Tax', 'cost': 0, 'location': 38, 'type': 'tax', 'base_rent': 75,
             'group': 'chill'},
            {'name': 'Boardwalk', 'cost': '400', 'location': 39, 'type': 'property',
                'base_rent': '50', 'group': 'darkblue', 'owner': None}
        ]


class Player:

    def __init__(self, name, token):
        self.computer = False
        self.properties = []
        self.position = 0
        self.money = 1500
        self.name = name
        self.token = token

    def roll_die(self):
        self.dieone = random.randint(1, 6)
        self.dietwo = random.randint(1, 6)
        self.doubles = False
        self.total = self.dieone + self.dietwo

        if self.dieone == self.dietwo:
            self.doubles == True
        return self.total  # , self.doubles deal with later for human players

    def update_position(self):
        self.update = self.roll_die()
        self.position = (self.position + self.update) % 40

    def print_player(self):
        print("Player {}: \n Properties: {} \n Board position: {} \n Money: {} \n Token: {} \n ".format(
            self.name, self.properties, self.position, self.money, self.token))


class GameState:
    def __init__(self):
        self.num_players = 0
        self.player_name = ''
        self.player_token = ''
        self.tokens = ['iron', 'doggie', 'top hat', 'cannon',
                       'wheelbarrow', 'battleship', 'thimble', 'race car', 'shoe']
        self.self.num_comps= 0
        self.error_of_players = 0
        self.total_players = 0
        #self.playerone
        #self.playertwo
        #self.playerthree
        #self.playerfour
    # call first

    def addHPlayers(self):
        while True:
            self.num_players = input(
                "How many human players will be playing? ")
        # create instance of a player, set computer value to false
            try:
                int(self.num_players)
                self.num_players = int(self.num_players)
                if self.num_players >= 0 and self.num_players < 5:
                    break
                else:
                    raise GenErr
            except ValueError:
                print("That's a string ")
            except GenErr:
                print(
                    "Number of players error. Please enter a number between 1 and 4")
    # call second

    def nameHPlayers(self):
        for i in range(self.num_players):
            self.player_name = input("Please enter a name: ")
            self.player_token = input(
                "Please choose a token from the list %s " % self.tokens)
            while True:
                try:
                    if self.player_token in self.tokens:
                        self.tokens.remove(self.player_token)
                        print("%s" % self.tokens)  # Used for debugging
                        break
                    else:
                        raise GenErr
                except GenErr:
                    print("Player token error.")
                    self.player_token = input(
                        "Please choose a token still available from the list %s " % self.tokens)

    def initHPlayers(self):
        for i in range (self.num_players):
            if i == 0:
                self.playerone = Player(self.player_name, self.player_token)
                self..append(self.playerone)
                self.playerone.print_player()
            elif i == 1:
                self.playertwo = Player(self.player_name, self.player_token)
                self..append(self.playertwo)
                self.playertwo.print_player()
            elif i == 2:
                self.playerthree = Player(self.player_name, self.player_token)
                self..append(self.playerthree)
                self.playerthree.print_player()
            elif i == 3:
                self.playerfour = Player(self.player_name, self.player_token)
                self..append(self.playerfour)
                self.playerfour.print_player()

    def initCPlayers(self):
        while True:
            self.num_comps = input("How many computer players will be playing? ")
            try:
                int(self.num_comps)
                self.num_comps = int(self.num_comps)
                self.error_of_players = 4 - self.num_players
                self.total_players = self.num_comps + self.num_players
                if self. > 0 and self. < 5:
                    break
                else:
                    raise GenErr
            except ValueError:
                print("That's a string ")
            except GenErr:
                print("Number of players error. Please enter a number between 0 and {}".format(
                    self.error_of_players))

        for i in range(self.num_comps):
            # computer name
            comp_name = random.choice(tokens)
            tokens.remove(comp_name)

            if i == 0:
                compone = Player(comp_name, comp_name)
                self..append(compone)
                compone.print_player()
            elif i == 1:
                comptwo = Player(comp_name, comp_name)
                self..append(comptwo)
                comptwo.print_player()
            elif i == 2:
                compthree = Player(comp_name, comp_name)
                self..append(compthree)
                compthree.print_player()
            elif i == 3:
                compfour = Player(comp_name, comp_name)
                self..append(compfour)
                compfour.print_player()



# Initialize game
# tokens = ['iron', 'doggie', 'top hat', 'cannon',
 #         'wheelbarrow', 'battleship', 'thimble', 'race car', 'shoe']

self. = []  # use the list index to implement turns

gameboard = GameBoard()
gamestate = GameState()

gamestate.addHPlayers()
gamestate.nameHPlayers()
gamestate.initHPlayers()
# really missing switches rn
#  if i == 0:
#     self.playerone = Player(player_name, player_token)
#    self..append(self.playerone)
#   self.playerone.print_player()
# elif i == 1:
#   self.playertwo = Player(player_name, player_token)
#  self..append(self.playertwo)
# self.playertwo.print_player()
# elif i == 2:
#    self.playerthree = Player(player_name, player_token)
#   self..append(self.playerthree)
#  self.playerthree.print_player()
# elif i == 3:
#    self.playerfour = Player(player_name, player_token)
#   self..append(self.playerfour)
#  self.playerfour.print_player()

# still need to fix this

'''\]
while True:
    self.num_comps = input("How many computer players will be playing? ")
    try:
        int(self.num_comps)
        self.num_comps = int(self.num_comps)
        self.error_of_players = 4 - num_players
        self. = self.num_comps + num_players
        if self. > 0 and self. < 5:
            break
        else:
            raise GenErr
    except ValueError:
        print("That's a string ")
    except GenErr:
        print("Number of players error. Please enter a number between 0 and {}".format(
            self.error_of_players))

for i in range(self.num_comps):
    # computer name
    comp_name = random.choice(tokens)
    tokens.remove(comp_name)

    if i == 0:
        compone = Player(comp_name, comp_name)
        self..append(compone)
        compone.print_player()
    elif i == 1:
        comptwo = Player(comp_name, comp_name)
        self..append(comptwo)
        comptwo.print_player()
    elif i == 2:
        compthree = Player(comp_name, comp_name)
        self..append(compthree)
        compthree.print_player()
    elif i == 3:
        compfour = Player(comp_name, comp_name)
        self..append(compfour)
        compfour.print_player()

# need to fix this but test on computer players for now

compone.update_position()
compone.print_player()

# if gameboard.tiles[compone.position] > 0:
#   compone.print_player()
game_space = gameboard.tiles[compone.position]  # this is a dictionary

# implemts the forced fee spaces
if game_space['location'] == 4 or game_space['location'] == 38:
    if game_space['location'] == 4:
        compone.money = compone.money - 100
    if game_space['location'] == 38:
        compone.money = compone.money - 200

# implements landing on go (put it after first turn) -> use total turns
if game_space['location'] == 0:
    compone.money = compone.money + 200

# for comp players
if game_space['cost'] != 0 and int(game_space['cost']) < compone.money:
    compone.money = compone.money - int(game_space['cost'])
    compone.properties.append(game_space)
    compone.print_player()
'''