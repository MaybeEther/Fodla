# SimpleDungeon.py

import random

def main():
    encounterProb = 80  # probability of encountering a monster
    monsterDictionary = loadMonsterDictionary()
    
    print("**** Welcome to Fódla ****")
    step = 0
    while step < 10:
        choice = mainMenu()
        if random.randint(0, 100) < encounterProb:
            battle(monsterDictionary)
        else:
            print("\nThe room is empty.")
        printPlayerStats()
        step = step + 1
    print("\nYou exit ...")


# The loadMosterDictionary() function returns a hard-coded dictionary
# For 5 points, it could read a file and load a better dictionary
def loadMonsterDictionary():
    md = {"Skeleton":[20, 3, 6, 0, 4, 5, 10],
          "Zombie":[10, 4, 8, 2, 7, 10, 20]}
    return md


# The mainMenu() function displays a menu and returns the desired move
def mainMenu():
    move = input("Move (n)orth, (s)outh, (e)ast, (w)est, or (r)est>")
    return move


# The printPlayerStats() function shows the player's info
def printPlayerStats():
    print("\nStats\n")


# The battle() function needs to loop until there is a winner
def battle(md):
    mKey = selectMonster(md)
    print("\nYou have encountered a", mKey)


# The selectMonster() function takes a dictionary as an argument.
# It returns a randomly selected key (a monster name).
# You are allowed to use this function as is.
def selectMonster(md):
    # Create 2d list of monster names and likelihoods.
    allMonsters = []
    for key in md:
        allMonsters.append([key, md[key][0]])
    # Find total of all likelihoods.
    total = 0
    for m in allMonsters:
        total = total + m[1]
    # Randomly, generate a number within the total
    selection = random.randint(0, total-1)
    # find the key based on random number
    highpoint = 0
    for m in allMonsters:
        highpoint = highpoint + m[1]
        if selection < highpoint:
            return m[0]

main()
