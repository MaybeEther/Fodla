import os
import random

def main():
    os.system("clear")
    print("                        **** Welcome to Fódla ****")
    print(" *** For 800 years the huns have ruled and terrorized the people of Fódla ***")
    print("*** but today on the 113th day of the year the 7 wise men have called for ***")
    print("         *** every true born man and women of Fódla to rise ***")
    input("\n\nPress Enter to continue...")
    os.system("clear")
    floorOne()
    print("\nCongratulations you won Fódlas independence ! (or there is no more content)")


def floorOne():
    Neirb = {"Neirb": [10,8,6]}
    print("Tomás: Hello there young Fódlian, before you get into Dubh Linn you will need to take out the guard")
    input("\n\nPress Enter to continue...")
    os.system("clear")
    battle(Neirb)
    mainMenu()


def loadMonsterDictionary():
    hun = {"health": [20], "maxHealth": [20], "Strength": [1], "Luck": [1]}
    hun_spell = {"health": [20], "maxHealth": [20], "Strength": [1], "Luck": [1]}
    hun_chariot = {"health": [20], "maxHealth": [20], "Strength": [1], "Luck": [1]}

    md = {"Hun": hun,
          "Hun Spell Caster": hun_spell,
          "Hun War Chariot": hun_chariot
          }

    return md


def mainMenu():
    move = input("Move (f)oward, (s)kills  or (i)nventory> ")
    if move == "i":
        printPlayerStats()




def printPlayerStats():
    md = loadMonsterDictionary()
    os.system("clear")
    player = {"health": [20], "maxHealth": [20], "Strength": [1], "Luck": [1]}
    print(f'''
Player Stats
-------------
Health = {player["health"]} / {player["maxHealth"]}
Power = {player["Strength"]}
Luck level = {player["Luck"]}

{md[0]}
''')




def battle(md):
    mKey = md
    if mKey == "Hun Sniper":
        print("")
    print("\nYou have encountered a", mKey)


def selectMonster(md):
    allMonsters = []
    for key in md:
        allMonsters.append([key, md[key][0]])
    total = 0
    for m in allMonsters:
        total = total + m[1]
    selection = random.randint(0, total - 1)
    highpoint = 0
    for m in allMonsters:
        highpoint = highpoint + m[1]
        if selection < highpoint:
            return m[0]


main()
