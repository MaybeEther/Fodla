#Name Duncan
# a game of sorts
#level i tried for 75% + a story(5) + monster file(5) + multiple attacks(5) + retreat failure(5) + shop(5) total = 100%
import os
import random
import time
import DndTypes


def main():
    os.system("clear")
    print("                        **** Welcome to Fódla ****")
    print(" *** For 800 years the huns have ruled and terrorized the people of Fódla ***")
    print("*** but today on the 113th day of the year the 7 wise men have called for ***")
    print("         *** every true born man and women of Fódla to rise ***")
    input("\n\nPress Enter to continue...")
    os.system("clear")
    floor_one()
    print("\nCongratulations you won Fódlas independence ! (or there is no more content)")


def floor_one():
    print("Tomás: Hello there young Fódlian, before you get into Dubh Linn you will need to take out the guard")
    input("\n\nPress Enter to continue...")
    os.system("clear")
    shop()
    battle(load_monster_dictionary()["Neirb"])
    main_menu()
    battle(load_monster_dictionary()["Hun"])
    main_menu()
    battle(load_monster_dictionary()["Hun Spell Caster"])
    shop()
    main_menu()
    battle(load_monster_dictionary()["Hun War Cart"])
    main_menu()
    battle(load_monster_dictionary()["Maxwell The Hun"])
    main_menu()
    battle(load_monster_dictionary()["Nathen The Hun"])
    main_menu()
    battle(load_monster_dictionary()["French The Hun"])
    main_menu()
    battle(load_monster_dictionary()["Friend The Hun"])
    main_menu()
    battle(load_monster_dictionary()["Lowe The Hun"])
    main_menu()
    battle(load_monster_dictionary()["Wimborne The Hun"])
    main_menu()
    battle(load_monster_dictionary()["Neirb"])
    # ik i could have just used the moster select however i wanted structured progression rather then randomness


def load_monster_dictionary():
    monsters: dict[str, DndTypes.Monster] = {
        singleton(DndTypes.Monster1).name: singleton(DndTypes.Monster1),
        singleton(DndTypes.Monster2).name: singleton(DndTypes.Monster2),
        singleton(DndTypes.Monster3).name: singleton(DndTypes.Monster3),
        singleton(DndTypes.Monster4).name: singleton(DndTypes.Monster4),
        singleton(DndTypes.Monster5).name: singleton(DndTypes.Monster5),
        singleton(DndTypes.Monster6).name: singleton(DndTypes.Monster6),
        singleton(DndTypes.Monster7).name: singleton(DndTypes.Monster7),
        singleton(DndTypes.Monster8).name: singleton(DndTypes.Monster8),
        singleton(DndTypes.Monster9).name: singleton(DndTypes.Monster9),
        singleton(DndTypes.Monster10).name: singleton(DndTypes.Monster10)
    }
    return monsters

def main_menu():
    standard = standard_attacks()
    i = 0
    while i == 0: # starts an infinit loop so the only way out is moving foward
        move = input("Move (f)orward, (s)kills  or (i)nventory> ")
        while move != "f" and move != "i" and move != "s":
            move =input("Move (f)orward, (s)kills  or (i)nventory> ONLY ")
        if move == "s":
            os.system("clear")
            print(f"health: {get_player().health}")
            print(f"cash: {get_player().cash}")
            print(f"level: {get_player().level}")
            input("press anything to continue")
        elif move == "i":
            for x in standard:
                if standard[x].unlocked == True:
                    print(x + ": " + standard[x].name)
        elif move == "f":
            i = 1

def battle(md: DndTypes.Monster):
    local_health = md.health
    standard = standard_attacks()
    e = 0
    sniper = 0
    os.system("clear")
    print(f"you have run into {md.name}")
    while int(get_player().health) > 0 and int(local_health) > 0 and e != 1:
        if md.name == "Hun Spell Caster" and sniper == 0:
            print("*ping* a long range spell hits you dealing 10 damage")
            get_player().health -= 10
            if get_player().health <= 0:
                death()
            print("Health now equals " + str(get_player().health))
            sniper +=1

        else:
            print("you can (f)ight or (r)un away")
            move = input("what is your opening move? ")
            while move != "r" and move != "f":
                move = input("try again. you may only enter r or f")
            if move == "r":
                if random.randint(0, 2) == 1:
                    print(f"you ran away. YAY! {md.name} ate ur dust!")
                    e = 1
                else:
                    input("you couldnt get away, prepare to fight, ready?")
                    move = "f"
            elif move == "f":
                os.system("clear")
                print(f"your options against {md.name} are:")
                for x in standard:
                    if standard[x].unlocked == True:
                        print(x +": "+standard[x].name)
                strike = input("which move would you like to use?")
                while not strike.isdigit() and strike <= len(standard):
                    strike = input("please say the corasponding number")
                local_health = int(local_health) - int(standard[strike].damage)
                print(f"{md.name}s health is now: {local_health}")
                if int(local_health) <= 0:
                    print(f"Congratulations you killed {md.name}! take 10 coins!")
                    get_player().cash += 10
                else:
                    print(f"the {md.name} fires back! dealing {md.max_health} damage!")
                    get_player().health -= int(md.max_health)
                    if get_player().health <= 0:
                        death()
                    print(f"your health is now {get_player().health}\n")



    if get_player().health < 0:
        death()

def select_monster(md):
    all_monsters = []
    for key in md:
        all_monsters.append([key, md[key][0]])
    total = 0
    for m in all_monsters:
        total = total + m[1]
    selection = random.randint(0, total - 1)
    highpoint = 0
    for m in all_monsters:
        highpoint = highpoint + m[1]
        if selection < highpoint:
            return m[0]

def standard_attacks():
    attacks: dict[str, DndTypes.StandardAttack] = {  # Same reasoning for typing as for SpecialAttacks
        "1": singleton(DndTypes.ZweiAttack),
        "2": singleton(DndTypes.BowAttack),
        "3": singleton(DndTypes.LightAttack),
        "4": singleton(DndTypes.ShortAttack)
    }
    return attacks


def singleton(cls):
    if cls not in DndTypes.instances:
        DndTypes.instances[cls] = cls()
        return DndTypes.instances[cls]
    return DndTypes.instances[cls]

def shop():
    standard = standard_attacks()
    # noinspection PyUnusedLocal

    os.system("clear")
    print("Muammar: Hello my friend! I have many fine wares for you to keep killing the huns!")
    i = 0
    while i <= 0:
        initial = input("Muammar: so what do you need? (w)epons,(s)pecial weapons or (e)xit ")
        while initial != "w" and initial != "s" and initial != "midas" and initial != "e":
            initial = input("Muammar: so what do you need? (w)epons,(s)pecial weapons or (e)xit ")
        if initial == "w":
            os.system("clear")
            # noinspection PyArgumentList
            print(f"you have " + str(get_player().cash) + " moonies")
            print("for you i have very special toys!")
            for x in standard:
                if not standard[x].unlocked:
                    print(f"{x}: " + standard[x].name + " " + str(standard[x].cost))

            while True:
                try:
                    order = int(input("Which move would you like to buy? (say the corresponding number) "))
                except ValueError:
                    print("SAY THE NUMBER")
                    continue
                if get_player().cash >= standard[order].cost:
                    while True:
                        try:
                            make_sure = input(f"Are you sure you want to buy a " + standard[order].name + " for " + str(standard[order].cost) + " gold Y/N? ONLY")

                        except ValueError:
                            print("SAY THE Y or N")
                            continue
                    if make_sure == "Y":
                        standard_attacks()[str(order)].unlocked = True
                        get_player().cash -= 500
                        input("press enter to restart")
                        break
                    else: input("ok then press anything to continue")
                else:
                    print("you cant afford that (ur poor)")
                    input("press enter to restart")
                break

        elif initial == "midas":  # cheat code for free money! (debug only stay away players!!!
            print("Oh hi midas here take 500 gold")
            get_player().cash += 500
            input("press enter to restart")
        elif initial == "e":
            i += 1


def get_player():
    player: DndTypes.Player = singleton(DndTypes.Player)
    return player

def death():
    print(f"have died. at lvl " + str(get_player().level))
    time.sleep(10)
    os.system("clear")
    quit()

if __name__ == "__main__":
    DndTypes.load_monsters()
    main()
