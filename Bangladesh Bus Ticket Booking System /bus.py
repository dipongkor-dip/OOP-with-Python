from users import Passenger


class Bus:
    def __init__(self, number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0

    def available_seats(self):
        return self.total_seats - self.booked_seats

    def book_seat(self):
        if self.total_seats - self.booked_seats:
            self.booked_seats += 1
            return True
        else:
            return False


class BusSystem:
    def __init__(self, systemName):
        self.name = systemName
        self.busses = []
        self.passengers = []

    def book_ticket(self, bus_number, name, phone):
        av = False

        for bus in self.busses:
            if bus.number == bus_number:
                avs = bus.available_seats()
                if avs > 0:
                    bus.book_seat()

                    passenger = Passenger(name, phone)
                    self.passengers.append(passenger)
                    print("Seat Booked")

                    av = True
                else:
                    print("This Bus All Seats Booked")
                break

        if av == False:
            print("Invalid Bus Number")

    def add_bus(self, number, route, seats):
        bus = Bus(number, route, seats)
        self.busses.append(bus)
        print("Bus Added")

    def show_buses(self):
        print("========== All Busses =========")
        print("Bus Number\tAvailable seats")
        for bus in self.busses:
            print(f"{bus.number}\t\t{bus.total_seats - bus.booked_seats}")
