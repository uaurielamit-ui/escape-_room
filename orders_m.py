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
            add_new_order(import_orders())
        elif client_choice =="2":
            show_all_the_orders(import_orders())
        elif client_choice == "3":
            serch_order_by_id(import_orders())
        elif client_choice == "4":
            client_order(import_orders())
        elif client_choice == "5":
            show_order_by_date(import_orders())
        elif client_choice == "6":
            change_order(import_orders())
        elif client_choice == "7":
            print(cencel_order(import_orders()))
        else:
            print("wrong choice try agen ")



def import_orders():
    orders = storage.load_data("booking.json")
    return orders


def add_new_orders_id(orders):
    max_id = 0
    for order in orders:
        if int(order ["booking_id"][1:]) >= max_id:
            max_id = int(room ["booking_id"][1:])+1
    return "B" + str(max_id).zfill(3)


def add_new_order(orders):
    ...

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


def change_order(orders):
    ...

def cencel_order(orders:list):
    client_choice = val.val_str("enter the id of the order to cencel: ")
    if_in = 0
    for order in orders:
        if client_choice == order["booking_id"]:
            order["status"] = "Cancelled"
            storage.dump_data(orders, "booking.json")
            return "canseling secsis"
    return "item did not found "
        


