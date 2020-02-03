#captain crunch

from random import randint
game_running = True
from Game import *
def Champion():
    #champion combat
    def calculate_monster_attack():
        return randint(monster["attack_min"], monster["attack_max"])
    #calculates evasion from 3-20

    def calculate_evasion():
        return randint(player["evasion_min"],player["evasion_max"])

    #calculates monsters attack from 10-18
    game_running = True
    while game_running == True:
        new_round = True
        player = {"name": "Nick", "attack": 15, "heal": 15, "health": 100, "evasion_min": 5, "evasion_max": 18}
        monster = {"name": "Champion", "attack_min": 10, "attack_max": 18, "health": 100}

        print("---" * 7)
        print("What is your name o warrior? Roars the Nytseny Champion")
        print("Tell me you name, ssssoo I can praise you for offering yoursssself as sssssacrifice!(Enter name)")
        player["name"] = input()
        print(player["name"] + " has " + str(player["health"]) + " HP")
        print(monster["name"] + " has " + str(monster["health"]) + " HP")

        while new_round == True:

            player_won = False
            monster_won = False
            print("______"*5)
            print("Please choose your course of action")
            print("1) Attack")
            print("2) Heal")
            print("3) Evade")
            print("______"*5)
            player_choice = input()

            if player_choice == "1":
                monster_attack = randint(monster["attack_min"],monster["attack_max"])
                monster["health"] = monster["health"]  - player["attack"]
                if monster["health"] <= 0:
                    player_won = True
                else:
                    player["health"] = player["health"] - calculate_monster_attack()
                    if player["health"] <= 0:
                        monster_won = True


            elif player_choice == "2":
                player["health"] = player["health"] + player["heal"]

                player["health"] = player["health"] - calculate_monster_attack()
                if player["health"] <= 0:
                    monster_won = True

            elif player_choice == "3":
                player["health"] = player["health"] - calculate_monster_attack() + calculate_evasion()
                if player["health"] <= 0:
                    monster_won = True


            else:
                print("Invalid Input")
            if player_won == False and monster_won == False:
                print(player["name"] + " has " + str(player["health"]) + " left" )
                print(monster["name"] + " has " + str(monster["health"]) + " left")
            elif player_won:
                print(player["name"] +  " has won")
                print("Combat has ended")
                new_round = False
                game_running = False

            if monster_won:
                print("The monster has won")
                new_round = False
                game_running = False
                Game.death()




