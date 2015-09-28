__author__ = 'ab53995'

# 1 - Norr 2 - Öster 3 - Söder 4 - Väster

inventory_list = []


# def lock():
#    if inventory_list[0] == "Key":
#        return 3
#    return 2


item = ["Key"]

room_list = []
room = ["\nYou see a light down a narrow tunnel to the north." , 1, None, None, None, item]
room_list.append(room)

room = ["\nYou can see the line of torches continuing further to the north", 2, None, 0, None, None]
room_list.append(room)

room = ["\nYou see a great iron door. It has no doorknob, only one large keyhole", 4, None, 1, None, None]
room_list.append(room)

room = ["\nYou unlocked the iron door with your key. \nBeyond the door lies endless treasures. Your adventure has been very fruitful and you retire to a castle by the sea.", None, None, None, None]
room_list.append(room)

room = ["\nYou fail to open the door, it appears to be locked", 2, None, 1, None, None]
room_list.append(room)

current_room = 0

done = False

winds = ("north", "east", "west", "south")

print("You wake up in a dark dungeon.")
while not done:
    print(room_list[current_room][0])
    if current_room == 3:
        break

    answer = input("What do you want to do?\n").lower()

    if answer == "q":
        break

    elif answer == "north":
        next_room = room_list[current_room][1]
        if next_room is None:
            print("You can't go that way")
            continue
        current_room = next_room

    elif answer == "east":
        next_room = room_list[current_room][2]
        if next_room is None:
            print("You can't go that way")
            continue
        current_room = next_room

    elif answer == "south":
        next_room = room_list[current_room][3]
        if next_room is None:
            print("You can't go that way")
            continue
        current_room = next_room

    elif answer == "west":
        next_room = room_list[current_room][4]
        if next_room is None:
            print("You can't go that way")
            continue
        current_room = next_room

    elif answer == "inventory":
        if inventory_list is None:
            print("Your inventory is empty")
            continue
        print(inventory_list, )

    elif answer == "take":
        item_take = room_list[current_room][5]
        if item_take is None:
            print("There is nothing to take here")
            continue
        inventory_list.append(room_list[current_room][5])
        print("You picked up a", room_list[current_room][5])
        room_list[2][1] = 3
        # Öppnar dörren
        room_list[current_room][5] = None


    elif answer == "look":
        if room_list[current_room][5] is not None:
            print("There is a", room_list[current_room][5], "on the ground")
        else:
            print("There's nothing here")

    # elif answer in winds:
    # kan förenkla skrivsättet för gång
    # vill kunna kolla åt olika håll och se vad det ser ut att finnas där?



    if answer == "help":
        print("\nYou can go in 4 different directions: North, East, South and West")
        print("If you want to pick up something write take")
        print("To quit press q")
        print("To check inventory type inventory")
        print("Type look to see if there's a object in the room.")
        print("Win by finding the treasure")



