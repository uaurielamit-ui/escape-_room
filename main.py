import rooms_m
def main():
    stop = False
    while not stop:
        client_choice = input("""
       
        Escape Room Management
     
        0. for exit 
        1. for rooms management
        """)

        if client_choice == "0":
            stop = True 
            break
        elif client_choice == "1":
            rooms_m.rooms_main()






if __name__ == ("__main__"):
    main()
