__author__ = 'ab53995'

# 1 - Norr 2 - Öster 3 - Söder 4 - Väster

def key():



inventory_list = []
item = ["Key"]

room_list = []
room = ["You wake up in a dark dungeon. You see the light of flickering torches in the north. There is a key on the ground" , 1, None, None, None, item]
room_list.append(room)

room = ["The light came from a nearly burned out torch. You can see the line of torches continuing further down in the dungeon", 2, None, 0, None, None]
room_list.append(room)

room = ["The torches lead up to a great iron door.", 3, None, 1, None, None]
room_list.append(room)

room = ["Beyond the door lies endless treasures. Your adventure has been very fruitful and you retire to a castle by the sea.", None, None, None, None]
room_list.append(room)





current_room = 0

done = False

while not done:
    print(room_list[current_room][0])
    if current_room == 3:
        break

    answer = input("What do you want to do?\n").lower()

    if answer == "q":
        break

    elif answer == "north":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You can't go that way")
            continue
        current_room = next_room

    elif answer == "east":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You can't go that way")
            continue
        current_room = next_room

    elif answer == "south":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You can't go that way")
            continue
        current_room = next_room

    elif answer == "west":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You can't go that way")
            continue
        current_room = next_room

    elif answer == "inventory":
        print(inventory_list[0][0])

    elif answer == "take":
        item_take = room_list[current_room][5]
        if item_take == None:
            print("There is nothing to take here")
        inventory_list.append(room_list[current_room][5])

    if answer == "help":
        print("\nYou can go in 4 different directions: North, East, South and West")
        print("If you want to pick up something write take")
        print("To quit press q")
        print("To check inventory type inventory")



