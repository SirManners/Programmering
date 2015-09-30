__author__ = 'ab53995'

# 1 - Norr 2 - Öster 3 - Söder 4 - Väster

inventory_list = []


# def lock():
#    if inventory_list[0] == "Key":
#        return 3
#    return 2


# Saker du kan göra:  Lägga till strider

turn = 1

item1 = "Key"
item2 = "Sword"

room_list = []
room = ["You see a light down a narrow tunnel to the north.", 1, None, None, None, None]
room_list.append(room)

room = ["You can see the line of torches continuing further to the north, and a doorway to the east", 2, 5, 0, None, item2]
room_list.append(room)

room = ["You see a great iron door. It has no doorknob, only one large keyhole", 4, None, 1, None, None]
room_list.append(room)

room = ["You unlocked the iron door with your key. \nBeyond the door lies endless treasures. Your adventure has been very fruitful and you retire to a castle by the sea.", None, None, None, None]
room_list.append(room)

room = ["You fail to open the door, it appears to be locked", 2, None, 1, None, None]
room_list.append(room)

room = ["A huge troll is blocking the way forward. The only way forward is to fight him.", None, 6, None, 1, None]
room_list.append(room)

room = ["The troll smashes you in the head with his club and you are fucking dead.", None, None, None, 5, item1]
room_list.append(room)


# Få den att printa items i rummet ifall de ligger där, lägg till combat mot trollet

current_room = 0

done = False

winds = ("north", "east", "west", "south")

print("\nYou wake up in a dark dungeon.\n")
while not done:
    print("\nTurn", turn)
    print(room_list[current_room][0])
    # print(current_room)
    if room_list[current_room][2] == 10 or current_room == 7:
        break

    while not done:
        answer = input("What do you want to do?\n").lower()

        if answer == "q":
            done = True
            break

        elif answer == "north":
            next_room = room_list[current_room][1]
            if next_room is None:
                print("You can't go that way")
                continue
            current_room = next_room
            break

        elif answer == "east":
            next_room = room_list[current_room][2]
            if next_room is None:
                print("You can't go that way")
                continue
            current_room = next_room
            break

        elif answer == "south":
            next_room = room_list[current_room][3]
            if next_room is None:
                print("You can't go that way")
                continue
            current_room = next_room
            break
        elif answer == "west":
            next_room = room_list[current_room][4]
            if next_room is None:
                print("You can't go that way")
                continue
            current_room = next_room
            break
        elif answer == "inventory":
            if inventory_list is None:
                print("Your inventory is empty")
                continue
            print("You are currently holding the following:\n", inventory_list)

        elif answer == "take":
            item_take = room_list[current_room][5]
            if item_take is None:
                print("There is nothing to take here")
                continue
            inventory_list.append(room_list[current_room][5])
            print("You picked up a", room_list[current_room][5])
            if item_take == "Key":
                room_list[4][0] = "You unlocked the iron door with your key. \nBeyond the door lies endless treasures. Your adventure has been very fruitful and you retire to a castle by the sea."
                # Öppnar dörren
                room_list[4][2] = 10
                room_list[current_room][5] = None

            if item_take == "Sword":
                room_list[6][0] = "You killed the troll with your sword!"
                room_list[current_room][5] = None
                # room_list[5][0] = "The trolls corpse is still here, but it's not blocking the way."

        elif answer == "look":
            if room_list[current_room][5] is not None:
                print("There is a", room_list[current_room][5], "on the ground")
            else:
                print("There's nothing here")
                # elif answer in winds:
        # kan förenkla skrivsättet för gång
        # vill kunna kolla åt olika håll och se vad det ser ut att finnas där?

        elif answer == "help":
            print("\nYou can go in 4 different directions: North, East, South and West")
            print("If you want to pick up something write take")
            print("To quit press q")
            print("To check inventory type inventory")
            print("Type look to see if there's a object in the room.")
            print("Win by finding the treasure")

        elif answer == "":
            continue

        else:
            print("I don't know what that means")
            continue

    if answer in winds:
            turn += 1
