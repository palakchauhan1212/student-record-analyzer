class Reservation:
    def __init__(self):
        self.passenger_info = {}
        self.cancelled_seat = []
        self.list = []
        self.__passenger = ''
        self.seat = 0
        self.__counter = 0
    
    def booking(self):
        seats = int(input('Number of seats to be booked:'))
        for i in  range(seats):
            booking_name = input('Enter the name of the passenger:')
            self.__passenger = booking_name
            self.list.append(self.__passenger)
            x=0
            if self.list.count(self.__passenger)>1:
                x=2
            if x==2:
                print('Passenger already exists')
            else:
                self.seat = self.__counter
                self.__counter = self.__counter + 1
                self.passenger_info[self.seat] = self.__passenger
                print('Seat booked successfully')
    
    def cancelling(self):
        seats = int(input('Number of seats to be cancelled:'))
        for i in range(seats):
            cancelling_name = input('Enter the name of the passenger:')
            a=0
            for k,v in self.passenger_info.items():
                if v == cancelling_name:
                    cancel_seat = k
                    print('Ticket cancelled')
                    a+=1
            if a>0:
                del self.passenger_info[cancel_seat]
                self.cancelled_seat.append(cancel_seat)
                self.list.remove(cancelling_name)
            else:
                print('Passenger not present')
    
    def cancelled_seat_rebooking(self):
        print('Empty seat:',self.cancelled_seat)
        seats = int(input('Enter the number of seats to be booked:'))
        if seats <= len(self.cancelled_seat):
            for i in range(seats):
                rebooking_name = input('Enter the name of the passenger:')
                self.__passenger = rebooking_name
                self.list.append(self.__passenger)
                x=0
                if self.list.count(self.__passenger)>1:
                    x=2
                if x==2:
                    print('Passenger already exists')
                else:
                    for i in range(len(self.cancelled_seat)):
                        self.passenger_info[self.cancelled_seat[i]] = self.__passenger
                        self.cancelled_seat.remove(self.cancelled_seat[i])
                    print('Seat booked successfully')
        else:
            print(seats,'seats not available')

    def displaying(self):
        print('Passenger list displayed:',self.passenger_info)
        print('Empty seat:',self.cancelled_seat+1)
    
def main():
    system = Reservation()
    while True:
        print('''How can I help you?
        1. Press 1 for for Boooking a ticket
        2. Press 2 for Cancelling a ticket
        3. Press 3 for Booking cancelled seat
        4. Press 4 for Displaying Passengers detail
        5. Anything else for exit''')
        user_input = input('Enter your choice:')
        if user_input == '1':
            system.booking()
        elif user_input == '2':
            system.cancelling()
        elif user_input == '3':
            system.cancelled_seat_rebooking()
        elif user_input == '4':
            system.displaying()
        else:
            break
if __name__ == "__main__":
    main()