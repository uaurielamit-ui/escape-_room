import rooms_m
import orders_m
import data_stats
def main():
    stop = False
    while not stop:
        client_choice = input("""
       ========================
        Escape Room Management
       ========================
        0. for exit 
        1. for rooms management
        2. for orders managmante
        3. for data end statistics
        """)

        if client_choice == "0":
            stop = True 
            break
        elif client_choice == "1":
            rooms_m.rooms_main()
        elif client_choice == "2":
            orders_m.oeder_main()
        elif client_choice == "3":
            data_stats.data_main()




if __name__ == ("__main__"):
    main()
