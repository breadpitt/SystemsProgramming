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
        self.total_position = 0
        self.money = 1500
        self.name = name
        self.token = token
        self.passed_go = False
        self.landed_go = False

    def roll_die(self):
        self.dieone = random.randint(1, 6)
        self.dietwo = random.randint(1, 6)
        self.doubles = False
        self.die_return = []  # better than returning a tuple

        self.total = self.dieone + self.dietwo
        self.die_return.append(self.total)
        if self.dieone == self.dietwo:
            self.doubles == True
        self.die_return.append(self.doubles)
        return self.die_return

    def update_position(self, dice_result):
        self.dice_result = dice_result
        self.position = (self.position + self.dice_result)
        if self.position > 40:
            #self.passed_go = True  # be sure to reset
            self.position = self.position % 40
        if self.position == 40:
            #self.landed_go = True  # be sure to reset
            self.money = self.money + 200
            self.position = self.position % 40

    def print_player(self):
        print("Player {}: \n Properties: {} \n Board position: {} \n Money: {} \n Token: {} \n ".format(
            self.name, self.properties, self.position, self.money, self.token))

##########################################################################################################
# change the num_players implementation from 0-4 to 2-4


class GameState:
    def __init__(self):
        self.num_players = 0
        self.player_name = ''
        self.player_token = ''
        self.tokens = ['iron', 'doggie', 'top hat', 'cannon',
                       'wheelbarrow', 'battleship', 'thimble', 'race car', 'shoe']
        self.num_comps = 0
        self.error_of_players = 0
        self.total_players = 0
        self.turn_list = []

    def add_hplayers(self):
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

    def name_hplayers(self):
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

    def init_hplayers(self):
        for i in range(self.num_players):
            if i == 0:
                self.playerone = Player(self.player_name, self.player_token)
                self.turn_list.append(self.playerone)
                self.playerone.print_player()
            elif i == 1:
                self.playertwo = Player(self.player_name, self.player_token)
                self.turn_list.append(self.playertwo)
                self.playertwo.print_player()
            elif i == 2:
                self.playerthree = Player(self.player_name, self.player_token)
                self.turn_list.append(self.playerthree)
                self.playerthree.print_player()
            elif i == 3:
                self.playerfour = Player(self.player_name, self.player_token)
                self.turn_list.append(self.playerfour)
                self.playerfour.print_player()

    def init_cplayers(self):
        self.comp_name = ""
        while True:
            self.num_comps = input(
                "How many computer players will be playing? ")
            try:
                int(self.num_comps)
                self.num_comps = int(self.num_comps)
                self.error_of_players = 4 - self.num_players
                self.total_players = self.num_comps + self.num_players
                if self.num_comps > 0 and self.num_comps < 5:
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
            self.comp_name = random.choice(self.tokens)
            self.tokens.remove(self.comp_name)

            if i == 0:
                self.compone = Player(self.comp_name, self.comp_name)
                self.turn_list.append(self.compone)
                self.compone.print_player()
            elif i == 1:
                self.comptwo = Player(self.comp_name, self.comp_name)
                self.turn_list.append(self.comptwo)
                self.comptwo.print_player()
            elif i == 2:
                self.compthree = Player(self.comp_name, self.comp_name)
                self.turn_list.append(self.compthree)
                self.compthree.print_player()
            elif i == 3:
                self.compfour = Player(self.comp_name, self.comp_name)
                self.turn_list.append(self.compfour)
                self.compfour.print_player()

    def rollAndMove(self, Player):
        self.player = Player


class PropertyManagement:
    def __init__(self, GameBoard, AvailableProperties, Player, OwnedProperties, Players):
        # Actually want these variables to be shared across class instances
        available_properties = AvailableProperties
        owned_properties = OwnedProperties
        turn_list = Players

        self.no_cost_properties = [2, 7, 10, 17, 20, 22, 30, 33, 36]
        self.gameboard = GameBoard # could probably share this among class if need be
        self.current_player = Player
        self.current_property = {}

    def buy_property(self):      
        self.current_property = self.gameboard.tiles[self.current_player.position]  # get the property dictionary from the gameboard list at the current player's position
                     # implemts the forced fee spaces & go
        if self.current_property['location'] == 4 or self.current_property['location'] == 38 or self.current_property['location'] == 0:
            if self.current_property['location'] == 0:
                pass #self.current_player.money = self.current_player.money + 200
            elif self.current_property['location'] == 4:
                self.current_player.money = self.current_player.money - 100
            elif self.current_property['location'] == 38:
                self.current_player.money = self.current_player.money - 200

        # Player lands on a rent free / 0 cost property
        elif self.current_property['location'] in self.no_cost_properties: # 2, 7, 10, 17, 20 22, 30, 33, 36
            print("FREE RENT")
            pass

        elif self.current_property['location'] in owned_properties:
            # for i in turn_list:
             #    if self.current_property['location'] == i. 

        # for comp players
        elif self.current_property['cost'] != 0 and int(self.current_property['cost']) < self.current_player.money and self.current_property in available_properties.tiles:
            self.current_player.money = self.current_player.money - int(self.current_property['cost'])
            self.current_player.properties.append(self.current_property) # add to player profile so they can see what they own
            self.current_player.print_player()
            owned_properties[self.current_player.name] = self.current_property # key = player name value = dictionary of the property
            available_properties.tiles.remove(self.current_property)
           # for i in available_properties.tiles: looks like it's removing properly
            #    print(i)

    def print_owned_properties(self):
        #for k,v in owned_properties.items():
        #    print(k, v)
        print(owned_properties.items())

            


# Initialize game
gameboard = GameBoard()
available_properties = GameBoard()
owned_properties = {}
players = {}
#pfadf = PropertyManagement(gameboard)

gamestate = GameState()
# commenting for testing doo not delete
# gamestate.add_hplayers()
# gamestate.name_hplayers()
# gamestate.init_hplayers()
gamestate.init_cplayers()
print("DEBUG")
turn_list = gamestate.turn_list
rolling_player = turn_list[0]
prop_one = PropertyManagement(gameboard, available_properties, rolling_player, owned_properties, turn_list)
die_roll = rolling_player.roll_die()
rolling_player.update_position(die_roll[0])
prop_one.buy_property()
rolling_player.print_player()
prop_one.print_owned_properties()
#prop_one.print_owned_properties()
'''
for rolling_player in turn_list:
    doubles_count = 0
    die_roll = rolling_player.roll_die()
    rolling_player.update_position(die_roll[0])
    
    if die_roll[1] == True:
        rolling_player.doubles = False  # First thing first reset doubles bool
        print("DOUBLES!")
        die_roll = rolling_player.roll_die()
        rolling_player.update_position(die_roll)
        count += 1
    if die_roll[1] == True:
        rolling_player.doubles = False  # First thing first reset doubles bool
        die_roll = rolling_player.roll_die()
        rolling_player.update_position(die_roll)
        count += 1
        print("DOUBLE DOUBLES!!")
    if die_roll[1] == True:
        rolling_player.doubles = False  # First thing first reset doubles bool
        die_roll = rolling_player.roll_die()
        rolling_player.update_position(die_roll)
        print("TRIPLE DOUBLES!!! GO TO JAIL BUT NOT REALLY THAT IS HARD TO IMPLEMENT")
        if doubles_count == 2:  # 3rd doubles roll break
            doubles_count = 0
            continue
    print("END OF TURN \n")
    rolling_player.print_player()


'''