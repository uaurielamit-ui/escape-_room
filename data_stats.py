import orders_m
import val
def data_main():
    stop = False
    while not stop:
        client_choice = input("""
        =======================
            Orders  managment
        =======================
        0. for exit 
        1. sum activ orders
        2. sum canseld orders
        3. sum incum from active orders
        4. sum canceling fee
        5. the most orderd room
        6. sum orders per room
        7. Room occupancy rates
        """)

        if client_choice == "0":
            stop = True 
            break
        elif client_choice == "1":
            print(sum_activ_orders(orders_m.import_orders()))
        elif client_choice =="2":
            print(sum_canseld_orders(orders_m.import_orders()))
        elif client_choice == "3":
            print(sum_incum_from_active_orders(orders_m.import_orders()))
        elif client_choice == "4":
            print(sum_canceling_fee(orders_m.import_orders()))
        elif client_choice == "5":
            the_most_orderd_room(orders_m.import_orders())
        elif client_choice == "6":
            print(sum_orders_per_room(orders_m.import_orders()))
        elif client_choice == "7":
            print(cencel_order(import_orders()))
        else:
            print("wrong choice try agen ")

def sum_activ_orders(orders):
    sum_inv = 0
    for order in orders:
        if order["status"] == "Active":
            sum_inv +=1
    return f"you have a {sum_inv} orders "

def sum_canseld_orders(orders):
    sum_inv = 0
    for order in orders:
        if order["status"] == "Cancelled":
            sum_inv +=1
    return f"you have a {sum_inv} orders cancelled "

def sum_incum_from_active_orders(orders):
    sum_inv = 0
    for order in orders:
        if order["status"] == "Active":
            sum_inv += order["total_price"]
    return f"you have a {sum_inv} from all the active orders "

def sum_canceling_fee(orders):
    sum_inv = 0
    for order in orders:
        if order["status"] == "Cancelled":
            sum_inv += order["total_price"]
    return f"you have a {sum_inv} from all the cancelled orders "


def the_most_orderd_room(orders):
    ...
    # pop = []
    # m_pop = ""
    # for order in orders:
    #     pop[order["room_id"]] +=1
    # for p in pop.items:
    #     if p[]

    
def sum_orders_per_room(orders):
    sum_inv = 0
    room = val.val_str("enter the room id: ")
    for order in orders: 
        if order["room_id"] == room:
            sum_inv += 1
    return f" this room have {sum_inv} invaits"



