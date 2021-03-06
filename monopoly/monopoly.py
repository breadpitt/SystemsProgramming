#!/usr/local/bin/python3

import random
import pprint


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
        self.computer = True
        self.properties = []
        self.horizontal_list = []
        self.position = 0
        self.total_position = 0
        self.money = 1500
        self.name = name
        self.token = token
        self.passed_go = False
        self.landed_go = False
        self.rq = ""

    def roll_die(self):
        self.dieone = random.randint(1, 6)
        self.dietwo = random.randint(1, 6)
        self.doubles = False
        self.die_return = []  # better than returning a tuple
        
        self.die_return.append(self.dieone)
        self.die_return.append(self.dietwo)
        return self.die_return

    def update_position(self, dice_result):
        self.dice_result = dice_result
        self.position = (self.position + self.dice_result)
        if self.position > 40:
            # self.passed_go = True  # be sure to reset
            self.position = self.position % 40
        if self.position == 40:
            # self.landed_go = True  # be sure to reset
            self.money = self.money + 200
            self.position = self.position % 40

    def print_properties(self):
        for property_dict in self.properties:
            self.horizontal_list.append(property_dict['name'])
        print(self.horizontal_list)
        self.horizontal_list =[]

    def rage_quit(self):
            self.rq = input("Flip the table? y/n ")
            if self.rq == "y":
                print("(╯°□°）╯︵ ┻━┻\n")
                exit()

    def print_player(self):
        print("\n")
        print("Player {}: Properties:".format(self.name))
        self.print_properties()
        print("Money: {} Token: {} \n ".format(self.money, self.token))
        
    
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
                self.playerone.computer = False
                self.turn_list.append(self.playerone)
                self.playerone.print_player()
            elif i == 1:
                self.playertwo = Player(self.player_name, self.player_token)
                self.playertwo.computer = False
                self.turn_list.append(self.playertwo)
                self.playertwo.print_player()
            elif i == 2:
                self.playerthree = Player(self.player_name, self.player_token)
                self.playerthree.computer = False
                self.turn_list.append(self.playerthree)
                self.playerthree.print_player()
            elif i == 3:
                self.playerfour = Player(self.player_name, self.player_token)
                self.playerfour.computer = False
                self.turn_list.append(self.playerfour)
                self.playerfour.print_player()

    def init_cplayers(self):
        self.player_name = ""
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
            self.player_name = random.choice(self.tokens)
            self.tokens.remove(self.player_name)

            if i == 0:
                self.compone = Player(self.player_name, self.player_name)
                self.turn_list.append(self.compone)
                self.compone.print_player()
            elif i == 1:
                self.comptwo = Player(self.player_name, self.player_name)
                self.turn_list.append(self.comptwo)
                self.comptwo.print_player()
            elif i == 2:
                self.compthree = Player(self.player_name, self.player_name)
                self.turn_list.append(self.compthree)
                self.compthree.print_player()
            elif i == 3:
                self.compfour = Player(self.player_name, self.player_name)
                self.turn_list.append(self.compfour)
                self.compfour.print_player()
        #print("┬──┬◡ﾉ(° -°ﾉ)")
    
    def get_turnlist(self):
        return self.turn_list

 # or turn control       
class TurnControl:
    def __init__(self, Players, Player):
        turn_list = Players
        self.current_player = Player

    def get_turnlist(self):
        return turn_list

    def update_turnlist(self, turn_list, broke_player):
        turn_list.remove(broke_player)
        return turn_list

    def print_turnlist(self):
        print(turn_list)

    
class PropertyManagement:
    def __init__(self, GameBoard, Properties, Player, Players):
        # Actually want these variables to be shared across class instances
        available_properties = Properties
        # owned_properties = Properties
        turn_list = Players
        
        self.no_cost_properties = [2, 7, 10, 17, 20, 22, 30, 33, 36]
        self.gameboard = GameBoard  # could probably share this among class if need be
        self.current_player = Player
        self.current_property = {}
        self.landlord = ""
        self.player_eliminated = False
        self.buy = ""
    
    def buy_property(self):
        # get the property dictionary from the gameboard list at the current player's position
        self.current_property = self.gameboard.tiles[self.current_player.position]
                     # implemts the forced fee spaces & go
        if self.current_property['location'] == 4 or self.current_property['location'] == 38 or self.current_property['location'] == 0:
            if self.current_property['location'] == 0:
                self.print_location()
                print("+$200")
                pass  # self.current_player.money = self.current_player.money + 200
            elif self.current_property['location'] == 4:
                self.current_player.money = self.current_player.money - 100
                self.print_location();
                print("-$100")
            elif self.current_property['location'] == 38:
                self.current_player.money = self.current_player.money - 200
                self.print_location();
                print("-$200")
        # Player lands on a rent free / 0 cost property
        # 2, 7, 10, 17, 20 22, 30, 33, 36
        elif self.current_property['location'] in self.no_cost_properties:
            pass
            self.print_location()
            print("FREE RENT")
     
            
        elif self.current_property['owner'] != None and self.current_property['owner'] != self.current_player.name:
            self.current_player.money -= int(self.current_property['base_rent'])
            self.landlord = self.current_property['owner']
            if self.current_player.money > 0:
                for p in turn_list:
                    if p.name == self.landlord:
                        p.money += int(self.current_property['base_rent'])
                        #print("{} PAID {} ${} FOR RENT AT {}".format(self.current_player.name, self.landlord, self.current_property['base_rent'], self.current_property['name']))
            else:
                for p in turn_list:
                    if p.name == self.landlord:
                        p.money += self.current_player.money # transfer the remain amount of money
                        for pwnd in self.current_player.properties:
                            if pwnd in self.gameboard.tiles:
                                if pwnd['owner'] == self.current_player.name:
                                    #print("NEW OWNER OF {} IS {}".format(pwnd['name'], self.landlord))
                                    pwnd['owner'] = self.landlord
                                    p.properties.append(pwnd)
                self.player_eliminated = True
                return self.player_eliminated                
            
           
       
        elif self.current_property['cost'] != 0 and int(self.current_property['cost']) < self.current_player.money and self.current_property['owner'] == None:
            self.current_player.money = self.current_player.money - int(self.current_property['cost'])
            self.current_property['owner'] = self.current_player.name
            # add to player profile so they can see what they own
            self.current_player.properties.append(self.current_property)
           # self.current_player.print_player()
    
    def human_buy_property(self):
        #get the property dictionary from the gameboard list at the current player's position
        self.current_property = self.gameboard.tiles[self.current_player.position]
                     # implemts the forced fee spaces & go
        if self.current_property['location'] == 4 or self.current_property['location'] == 38 or self.current_property['location'] == 0:
            if self.current_property['location'] == 0:
                self.print_location();
                print("+$200")
                pass  # self.current_player.money = self.current_player.money + 200
            elif self.current_property['location'] == 4:
                self.current_player.money = self.current_player.money - 100
                self.print_location()
                print("-$100")
            elif self.current_property['location'] == 38:
                self.current_player.money = self.current_player.money - 200
                self.print_location();
                print("-$200")
        # Player lands on a rent free / 0 cost property
        # 2, 7, 10, 17, 20 22, 30, 33, 36
        elif self.current_property['location'] in self.no_cost_properties:
            pass
            self.print_location()
            print("FREE RENT")
            
        elif self.current_property['owner'] != None and self.current_property['owner'] != self.current_player.name:
            self.print_location()
            self.current_player.money -= int(self.current_property['base_rent'])
            self.landlord = self.current_property['owner']
            if self.current_player.money > 0:
                for p in turn_list:
                    if p.name == self.landlord:
                        p.money += int(self.current_property['base_rent'])
                        print("{} PAID {} ${} FOR RENT AT {}".format(self.current_player.name, self.landlord, self.current_property['base_rent'], self.current_property['name']))
            else:
                for p in turn_list:
                    if p.name == self.landlord:
                        p.money += self.current_player.money # transfer the remain amount of money
                        for pwnd in self.current_player.properties:
                            if pwnd in self.gameboard.tiles:
                                if pwnd['owner'] == self.current_player.name:
                                    print("NEW OWNER OF {} IS {}".format(pwnd['name'], self.landlord))
                                    pwnd['owner'] = self.landlord
                                    p.properties.append(pwnd)
                self.player_eliminated = True
                return self.player_eliminated                
            
           
       
        elif self.current_property['cost'] != 0 and int(self.current_property['cost']) < self.current_player.money and self.current_property['owner'] == None:
            self.print_location()
            self.buy = input("Would you like to buy the property? You currently have ${} y/n or p to print the property ".format(self.current_player.money))
            while self.buy != 'y' and self.buy !='Y' and self.buy != 'yes' and self.buy != 'n' and self.buy != 'N' and self.buy != 'no':
                if self.buy == 'p' or self.buy == 'P':
                    print(self.current_property)
                    self.buy = input("Would you like to buy the property? You currently have ${} y/n or p to print the property ".format(self.current_player.money))
                else:
                    print("Not a valid option. y/n/p")
                    self.buy = input("Would you like to buy the property? You currently have ${} y/n or p to print the property ".format(self.current_player.money))
            
            if self.buy == 'y' or self.buy =='Y' or self.buy == 'yes':
                self.current_player.money = self.current_player.money - int(self.current_property['cost'])
                self.current_property['owner'] = self.current_player.name
                # add to player profile so they can see what they own
                self.current_player.properties.append(self.current_property)
            if self.buy == 'n' or self.buy == 'N' or self.buy == 'no':
                print("Pass")
            
                
            

    def print_location(self):
        print("{} LANDED ON {}".format(self.current_player.name, self.current_property['name']));        
            


# Initialize game
gameboard = GameBoard()
properties = GameBoard()
# owned_properties = {}
players = {}
turn_list = []
gamestate = GameState()
print("Welcome to Monopoly")

# commenting for testing do not delete
gamestate.add_hplayers()
gamestate.name_hplayers()
gamestate.init_hplayers()
gamestate.init_cplayers()

turn_list = gamestate.get_turnlist()
numberofplayers = len(turn_list)
not_elimin_list = TurnControl(turn_list, turn_list[0])
eliminated = False
player_options = ""
#starts the game
while numberofplayers == len(turn_list) and len(turn_list) > 1:
    for rolling_player in turn_list:
        count = 0
        
        if rolling_player.computer == True:
            while count < 3:
                buy_or_rent = PropertyManagement(gameboard, properties, rolling_player, turn_list)
                die_roll = rolling_player.roll_die()
                
                print("{} rolled a {} {}".format(rolling_player.name, die_roll[0], die_roll[1]))
                if die_roll[0] == die_roll[1]:
                    print("DOUBLES")
                die_total = die_roll[0] + die_roll[1]
                rolling_player.update_position(die_total)
                eliminated = buy_or_rent.buy_property()
                if eliminated == True:
                    print("PLAYER {} HAS BEEN ELIMINATED ".format(rolling_player.name))
                    not_elimin_list.update_turnlist(turn_list, rolling_player) # subtract a player from turn list
                    print(len(turn_list))
                    numberofplayers = numberofplayers - 1
                    not_elimin_list = TurnControl(turn_list, turn_list[0])
                    eliminated = False
                    print("CURRENT STANDINGS ")
                    for i in turn_list:
                        if i.money > 0:
                            print("Player: {} has ${} and owns:".format(i.name, i.money))
                            i.print_properties()

                if die_roll[0] != die_roll[1]:
                    break
                if die_roll[0] == die_roll[1]:
                    print("REROLL!")    
                    count += 1
                


        else:
            while(count < 3):
                reroll = ""
                buy_or_rent = PropertyManagement(gameboard, properties, rolling_player, turn_list)
                player_options = input("Your Turn. Press 'r' to roll the die or 'p' to print your player information ")
                while player_options != 'r' and player_options  != 'R':
                    if player_options == 'p' or player_options == 'P':
                        rolling_player.print_player()
                        player_options = input("Your Turn. Press 'r' to roll the die or 'p' to print your player information ")
                    else:
                        print("{} is not a valid option. Please press 'r' or 'p'".format(player_options))
                        player_options = input("Your Turn. Press 'r' to roll the die or 'p' to print your player information ")

                die_roll = rolling_player.roll_die()
                print("{} rolled a {} {}".format(rolling_player.name, die_roll[0], die_roll[1]))
                if die_roll[0] == die_roll[1]:
                    print("DOUBLES")
                die_total = die_roll[0] + die_roll[1]
                rolling_player.update_position(die_total)
                eliminated = buy_or_rent.human_buy_property()
                if eliminated == True:
                    print("PLAYER {} HAS BEEN ELIMINATED ".format(rolling_player.name))
                    rolling_player.rage_quit()
                    not_elimin_list.update_turnlist(turn_list, rolling_player) # subtract a player from turn list
                    print(len(turn_list))
                    numberofplayers = numberofplayers - 1
                    not_elimin_list = TurnControl(turn_list, turn_list[0])
                    eliminated = False
                    print("CURRENT STANDINGS ")
                    for i in turn_list:
                        if i.money > 0:
                            print("Player: {} has ${} and owns:".format(i.name, i.money))
                            i.print_properties()
                
                if die_roll[0] == die_roll[1]:
                    reroll = input("You rolled DOUBLES. Roll again? y/n ")
                    if reroll == 'n':
                        break
                    else:
                        print("REROLL!")    
                        count += 1
                else:
                    break
                    



print("WINNER WINNER CHICKEN DINNER {} WON!".format(turn_list[0].name))

if turn_list[0].computer == False:
    flip_the_table = "n"
    flip_the_table = input("CELEBRATORY TABLE FLIP? y/n ")

    if flip_the_table == "y":
        print("(ﾉ´･ω･)ﾉ ﾐ ┸━┸")
        exit()