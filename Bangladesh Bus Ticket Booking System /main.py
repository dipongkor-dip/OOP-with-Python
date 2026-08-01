from bus import BusSystem
from users import Admin

busSystem = BusSystem("Bangladesh Bus Ticket Booking System")

while True:
    print(f"============= {busSystem.name} ==========")
    print("1. Admin Login")
    print("2. Book Ticket")
    print("3. View Buses")
    print("4. Exit")

    choice = int(input("Enter Your Choice: "))


    if choice == 1:
        username = input("Username: ")
        password = input("Password: ")

        ad = Admin()
        log = ad.login(username=username, password=password)

        if log:
            while True:
                print("================ Admin Menu =============")
                print("1. Add Bus")
                print("2. View All Buses")
                print("3. Logout")
    
                c = int(input("Enter Your Choice: "))
                if c == 1:
                    number = int(input("Enter Bus Number: "))
                    route = input("Enter Bus route: ")
                    seats = int(input("Enter Bus seats: "))
    
                    busSystem.add_bus(number, route, seats)
    
                elif c == 2:
                    busSystem.show_buses()
    
                elif c == 3:
                    break
                else:
                    print("Invalid Input")
        else:
            print("Invalid Credentials")

    elif choice == 2:
        bus_number = int(input("Enter Bus number: "))
        name = input("Enter Your name: ")
        phone = input("Enter Your Phone: ")

        busSystem.book_ticket(bus_number, name, phone)

    elif choice == 3:
        busSystem.show_buses()
    elif choice == 4:
        break
    else:
        print("Invalid Input")
