__author__ = 'ab53995'

# 1 - Norr 2 - Öster 3 - Söder 4 - Väster
room_list = []
room = ["You wake up in a dark dungeon. You see the light of flickering torches in the north" , 1, None, None, None, None]
room_list.append(room)

room = ["The light came from a nearly burned out torch. You can see the line of torches continuing further down in the dungeon", 1, None, 3, None, None]
room_list.append(room)

# room =

inventory_list = []
item = ["Key"]



current_room = 0



done = False

while done == False:
    print(room_list[current_room][0])
    answer = input("What do you want to do?").lower()
    if answer == "north":
        next_room = room_list[current_room][1]
        current_room = next_room
        if next_room == None:
            print("You can't go that way")

    elif answer == "east":
        next_room = room_list[current_room][2]
        current_room = next_room
        if next_room == None:
            print("You can't go that way")

    elif answer == "south":
        next_room = room_list[current_room][3]
        current_room = next_room
        if next_room == None:
            print("You can't go that way")

    elif answer == "west":
        next_room = room_list[current_room][4]
        current_room = next_room
        if next_room == None:
            print("You can't go that way")

    if answer == "q":
        break

    elif answer == "inventory":
        print(inventory_list)

    if answer == "help":
        print("You can go in 4 different directions: North, East, South and West\n")
        print("If you want to pick up something write grab\n")
        print("To quit press q\n")
        print("To check inventory type inventory\n")