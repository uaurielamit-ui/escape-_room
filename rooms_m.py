import storage
import val
def rooms_main():
    stop = False
    while not stop:
        client_choice = input("""
   
            Rooms  managment
      
        0. for exit 
        1. show all rooms
        2. scerch room
        3. add new room
        4. update room
        5. update room status
        """)

        if client_choice == "0":
            stop = True 
            break
        if client_choice == "1":
            show_all_rooms(import_rooms())
        if client_choice == "2":
            scerch_room(import_rooms())
        if client_choice == "3":
            print(add_new_room(import_rooms()))
        if client_choice == "4":
            update_room(import_rooms())
        if client_choice == "5":
            update_room_status(import_rooms())






def import_rooms():
    rooms = storage.load_data("rooms.json")
    return rooms



def show_all_rooms(rooms):
    for room in rooms:
        print(room)


def scerch_room(rooms):
    client_scerch = val.val_str("enter the room name: ").lower()
    if_in = 0
    for room in rooms:
        if client_scerch in room ["name"].lower():
            print(room)
            if_in += 1
    if if_in == 0:
        print("room not find ")


def add_new_room_id(rooms):
    max_id = 0
    for room in rooms:
        if int(room ["room_id"][1:]) >= max_id:
            max_id = int(room ["room_id"][1:])+1
    return "R" + str(max_id).zfill(3)


def add_difficolty():
    legal = False
    while not legal:
        client_choice = input(" esay =1 ,medium = 2, hard = 3")
        if client_choice == "1":
            return "Esay"
            legal = True
        if client_choice == "2":
            return "Medium"
            legal = True
        if client_choice == "3":
            return "Hard"
            legal = True


def add_new_room(rooms):
    room = {}
    room["room_id"] = add_new_room_id(rooms)
    room["name"] = val.val_str("enter the room name: ")
    room["difficulty"] = add_difficolty()
    room["duration"] =  val.val_int("add duration: ")
    room["min_players"] = val.val_int("add minimum players: ")
    room["max_players"] = val.val_int("add maxmum players: ")
    room["price_per_player"] = val.val_int("add price for player: ")
    room["is_active"]: True
    rooms.append (room)
    storage.dump_data(rooms, "rooms.json")
    return "room added"


def update_room(rooms):
    room_id = input("enter the room id: ")
    find = 0
    what_to_chang = input(" name = 1, difficolty = 2, duration = 3, min_players = 4, max_players = 5, price per person =6 ")
    for room in rooms:
        if room["room_id"] == room_id:
            if what_to_chang == "1":
                room["name"] = val.val_str("enter the room name: ")
                find += 1
            elif what_to_chang == "2":
                room["difficulty"] = add_difficolty()
                find += 1
            elif what_to_chang == "3":
                room["duration"] =  val.val_int("add duration: ")
                find += 1
            elif what_to_chang == "4":
                room["min_players"] = val.val_int("add minimum players: ")
                find += 1
            elif what_to_chang == "5":
                room["max_players"] = val.val_int("add maxmum players: ")
                find += 1
            elif what_to_chang == "6":
                room["price_per_player"] = val.val_int("add price for player: ")
                find += 1
            else:
                print("wrong choice ")
                return
            storage.dump_data(rooms, "rooms.json")
            print("changing sucses ")
    if find ==0:
        return print("room not find ") 

        
def update_room_status(rooms):
    room_id = input("enter the room id: ")
    find = 0
    what_to_chang = input("to activet the room press 1, to unactive the room pres 2")
    for room in rooms:
        if room["room_id"] == room_id:
            if what_to_chang == "1":
                room["is_active"] = True
                find +=1
            elif what_to_chang =="2":
                room["is_active"] = False
                find +=1
            else:
                print("wrong choice ")
                break
            storage.dump_data(rooms, "rooms.json")
            print("changing sucses ")
    if find == 0:
        print("room did not found ")