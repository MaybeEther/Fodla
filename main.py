import os
import random

def main():
    monsterDictionary = loadMonsterDictionary()

    print("                        **** Welcome to Fódla ****")
    print(" ***** For 800 years the huns have ruled and terrorized the people of Fódla *****")
    print("****** but today on the 113th day of the year the 7 wise men have called for ******")
    print("         ******* every true born man and women of Fódla to rise ********")
    input("\n\nPress Enter to continue...")
    os.system("clear")
    floorOne()
    print(name)
    print("\nCongratulations you won Fódlas independence ! (or there is no more content)")


def floorOne():
    Neirb = {"Neirb": [10, ]}
    print("Tomás: Hello there young Fódlian, before you get into Dubh Linn you will need to take out the guard")
    input("\n\nPress Enter to continue...")
    os.system("clear")
    battle(Neirb)


def loadMonsterDictionary():
    md = {"Hun": [20, 3, 6, 0, 4, 5, 10],
          "Hun Spell Caster": [10, 4, 8, 2, 7, 10, 20]}
    return md


def mainMenu():
    move = input("Move (f)oward, (s)kills  or (i)nventory>")
    return move


def printPlayerStats():
    os.system("clear")
    health = 20
    power = 20
    luck = 20
    
    print("\nStats\n")




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
