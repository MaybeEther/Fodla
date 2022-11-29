import os
import random

def main():
    monsterDictionary = loadMonsterDictionary()
    
    print("**** Welcome to Fódla ****")
    floorOne()
    print("\nCongratulations you won Fódlas independence ! (or there is no more content)")
def floorOne():


def loadMonsterDictionary():
    md = {"Skeleton":[20, 3, 6, 0, 4, 5, 10],
          "Zombie":[10, 4, 8, 2, 7, 10, 20]}
    return md

def mainMenu():
    move = input("Move (n)orth, (s)outh, (e)ast, (w)est, or (i)nventory>")
    return move

def printPlayerStats():
    print("\nStats\n")

def battle(md):
    mKey = selectMonster(md)
    print("\nYou have encountered a", mKey)
    
def selectMonster(md):
    allMonsters = []
    for key in md:
        allMonsters.append([key, md[key][0]])
    total = 0
    for m in allMonsters:
        total = total + m[1]
    selection = random.randint(0, total-1)
    highpoint = 0
    for m in allMonsters:
        highpoint = highpoint + m[1]
        if selection < highpoint:
            return m[0]

main()
