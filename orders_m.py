import val
import storage
def oeder_main():
    stop = False
    while not stop:
        client_choice = input("""
        =======================
            Orders  managment
        =======================
        0. for exit 
        1. add new order
        2. show all the orders
        3. serch order by id
        4. client order
        5. show order by date
        6. change order
        7. cencel order
        """)

        if client_choice == "0":
            stop = True 
            break
        elif client_choice == "1":
            print(add_new_order(import_orders(), import_rooms()))
        elif client_choice =="2":
            show_all_the_orders(import_orders())
        elif client_choice == "3":
            serch_order_by_id(import_orders())
        elif client_choice == "4":
            client_order(import_orders())
        elif client_choice == "5":
            show_order_by_date(import_orders())
        elif client_choice == "6":
            print(change_order(import_orders(), import_rooms))
        elif client_choice == "7":
            print(cencel_order(import_orders()))
        else:
            print("wrong choice try agen ")



def import_orders():
    orders = storage.load_data("booking.json")
    return orders


def import_rooms():
    rooms = storage.load_data("rooms.json")
    return rooms

#ולידציה של זמן
def add_new_orders_id(orders):
    max_id = 0
    for order in orders:
        if int(order ["booking_id"][1:]) >= max_id:
            max_id = int(order ["booking_id"][1:])+1
    return "B" + str(max_id).zfill(3)


def add_new_order(orders, rooms):
    the_room = if_room(rooms)
    quantety = if_quan_legal(the_room)
    order = {}
    order["booking_id"] = add_new_orders_id(orders)
    order["customer_name"] = val.val_str("enter the costamer name: ")
    order["room_id"] = the_room["room_id"]
    order["booking_date"] =  val.val_str("entaer the date: ")
    order["start_time"] = val.val_str("enter the time in dey: ")
    order["players"] = quantety
    order["total_price"] = total_price(the_room, quantety)
    order["status"] = "Active"
    order["cancellation_fee"] = 0.0
    orders.append (order)
    storage.dump_data(orders, "booking.json")
    return "order added"

def show_all_the_orders(orders):
    for order in orders:
        print(order)

def serch_order_by_id(orders):
    client_scerch = val.val_str("enter the order id: ")
    if_in = 0
    for order in orders:
        if client_scerch == order["booking_id"]:
            print(order)
            if_in += 1
    if if_in == 0:
        print("order not find ")


def client_order(orders):  
    client_scerch = val.val_str("enter the client name: ").lower()
    if_in = 0
    for order in orders:
        if client_scerch in order["customer_name"].lower():
            print(order)
            if_in += 1
    if if_in == 0:
        print("client not find ")


def show_order_by_date(orders):
    client_scerch = val.val_str("enter the order date like diss  2026-11-18: ")
    if_in = 0
    for order in orders:
        if client_scerch in order["booking_date"]:
            print(order)
            if_in += 1
    if if_in == 0:
        print("client not find ")


def change_order(orders, rooms):
    which_order = val.val_str("enter the order id you wwont to change: ")
    for order in orders:
        if order["booking_id"] == which_order:
            client_choice = val.val_str("1.change the name, 2.to change the room, 3.to change the date, 4.to change the time, 5.to caange the number of player:  ")
            if client_choice == "1":
                order["customer_name"] = val.val_str("enter the costamer name: ")
            elif client_choice == "2":
                order["room_id"] = if_room(rooms)
            elif client_choice == "3":
                order["booking_date"] =  val.val_str("entaer the date: ")
            elif client_choice == "4":
                order["start_time"] = val.val_str("enter the time in dey: ")
            elif client_choice == "5":
                the_room = ""
                for room in rooms:
                    if room ["room_id"] == order["room_id"]:
                        the_room = room
                quantety = if_quan_legal(the_room)
                order["players"] = quantety
                order["total_price"] = total_price(the_room, quantety)
            orders.append (order)
            storage.dump_data(orders, "booking.json")
            return "order added"
    return "order did not fownd "



#הוספת קנס ביטול הזמנה 
def cencel_order(orders:list):
    client_choice = val.val_str("enter the id of the order to cencel: ")
    if_in = 0
    for order in orders:
        if client_choice == order["booking_id"]:
            order["status"] = "Cancelled"
            storage.dump_data(orders, "booking.json")
            return "canseling secsis"
    return "item did not found "
        

def if_room(rooms):
    legal = False
    while not legal:
        choice = val.val_str ("enter the room id: ")
        for room in rooms:
            if room["room_id"] == choice and room["is_active"] == True:
                legal = True
                return room


def if_quan_legal(room):
    legal = False
    while not legal:
        player_num = val.val_int("enrer the player number: ")
        if player_num >= room["min_players"] and player_num <= room["max_players"]:
            legal = True
            return player_num
        


def total_price(room, quantety):
    total = room["price_per_player"] * quantety
    if quantety > 4 and quantety <= 6:
        total = round(total *0.9, 2)
    if quantety >= 7:
        total = round(total * 0.85, 2)
    return total







