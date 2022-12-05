import os
import random
import time

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
    Neirb = {"name": "Neirb", "health": 5, "maxHealth": 5, "Strength": 1, "Luck": 1}
    print("Tomás: Hello there young Fódlian, before you get into Dubh Linn you will need to take out the guard")
    input("\n\nPress Enter to continue...")
    os.system("clear")
    battle(Neirb)
    mainMenu()


def loadMonsterDictionary():
    hun = {"name": "Hun", "health": 20, "maxHealth": 20, "Strength": 1, "Luck": 1}
    hun_spell = {"name": "Hun Spell Caster","health": 20, "maxHealth": 20, "Strength": 1, "Luck": 1}
    hun_chariot = {"name": "Hun Armored Chariot","health": 20, "maxHealth": 20, "Strength": 1, "Luck": 1}

    md = {"Hun": hun,
          "Hun Spell Caster": hun_spell,
          "Hun War Chariot": hun_chariot
          }

    return md


def mainMenu():
    move = input("Move (f)oward, (s)kills  or (i)nventory> ")
    if move == "s":
        printPlayerStats()

def playerStats():
    player = {"health": 20, "maxHealth": 20, "Strength": 1, "Luck": 1, "XP": 0}
    return player

def level():
    XP = playerStats()
    lvl = round(XP["XP"] / 100)
    return lvl


def printPlayerStats():
    stats = playerStats()
    os.system("clear")
    print(f'''
Player Stats
-------------
Health = {stats["health"]} / {stats["maxHealth"]}
Power = {stats["Strength"]}
Luck level = {stats["Luck"]}
''')

def battle(md):
    mKey = md
    ps = playerStats()
    sta = standard_attacks()
    sA = special_attacks()
    while ps["health"] > 0:
        if mKey == "Hun Sniper":
            print("*ping* a long range spell hits you dealing 10 damage")
            ps.update({health: 10})
            if ps["health"] <= 0:
                death()
            print("Health now equals " + ps["health"])
        else:
            print("\nYou have encountered a", mKey[name])

    if ps["health"] <0:
        death()
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
def standard_attacks():
    short = {"unlocked": true, "DO": 5, name: "short sword"}
    zwei = {"unlocked": false, "DO": 30, name: "claidheamh mòr"}
    bow = {"unlocked": false, "DO": 8, name: "Bow And Arrow"}
    light = {"unlocked": false, "DO": 500, name: "Claidheamh Soluis"}
    standard = {"short": short, "zwei": zwei, "bow": bow, "light": light}
    return standard
def special_attacks():
    sunBurst = {"unlocked": false, "DO": 10, "mana": 30}
    ladies = {"unlocked": false, "DO": 30, "mana": 40}
    volunteers = {"unlocked": false, "DO": 80, "mana": 80}
    mellowDivision = {"unlocked": false, "DO": 50, "mana": 60}
    mrCoileáin = {"unlocked": false, "DO": 100, "mana": 130}
    secondaries = {"Sun Burst": sunBurst, "Cummann & mBan": ladies, "Fódla Volunteers": volunteers, "mellow": mellowDivision, "Collins": mrCoileáin}
    return secondaries
def shop():
    cash = wallet()
    os.system("clear")
    print("Muammar: Hello my friend! I have many fine wares for you to keep killing the huns!")
    initial = input("Muammar: so what do you need? (w)epons,(s)pecial wepons or (p)otions")
    while (initial != "w" and initial != "s" and initial != "p" and initial != "midas"):
        initial = input("Muammar: so what do you need? (w)epons,(s)pecial wepons or (p)otions")
    if initial == "w":
        print()
    elif initial == "s":
        print()
    elif initial == "p":
        print()
    elif initial == "midas":
        print()
def wallet():
    wallet = 0
    return wallet
def death():
    print(f"have died. at lvl " + str(level()))
    time.sleep(10)
    os.system("clear")
    quit()
main()
