from waitlist import Waitlist
class Menu:
    """A class representing the menu for the restaurant reservation program"""

    def __init__(self):
        """Initialize the menu with the waitlist object"""
        self.waitlist = Waitlist()

    def run(self):
        """Print the main menu"""
        print("Welcome to the Restaurant Reservation System!")
        print("==============================================")
        print("Please select an option:")
        print("1. Add a customer to the waitlist")
        print("2. Seat the next customer")
        print("3. Change the time of a customer's reservation")
        print("4. Peek at the next customer")
        print("5. Print the reservation list")
        print("6. Quit")
        print("")
        while True:
            
            choice = input("Enter your choice (1-6): ")
            print("*************************************************")
            #Each one of these options should call a method from Waitlist class 
            if choice == "1":
                #TODO """Add a customer to the waitlist"""
                name = input('Enter the customer\'s name: ')
                time = input('Enter the time of the reservation (HH:MM): ')
                result = self.waitlist.add_customer(name, time)
                while result == False:
                    time = input('Enter a valid time of the reservation (HH:MM): ')
                    result = self.waitlist.add_customer(name, time)
                print(f'\n{name} has been added to the wait list at {time}\n')
                

            elif choice == "2":
                #TODO"""Seat the next customer"""
                name, time = self.waitlist.seat_customer()
                if name or time is not None:
                    print(f'\nSeated customer: {name}, reservation time: {time}\n')
                else:
                    print(f'\nNo customers are on the waitlist\n')

            elif choice == "3":
                #TODO"""Change the time of a customer's reservation"""
                name = input('Enter the customer\'s name: ')
                new_time = input('Enter the new time of the reservation (HH:MM): ')
                while self.waitlist.validate_time(new_time) == False:
                    new_time = input('Enter a valid new time of the reservation (HH:MM): ')
                result = self.waitlist.change_reservation(name, new_time)
                if result is False:
                    print(f'\n{name} does not have a reservation listed\n')
                else:
                    print(f'\n{name}\'s reservation time has been changed to {new_time}\n')

            elif choice == "4":
                #TODO"""Peek at the next customer"""
                name, time = self.waitlist.peek()
                if name or time is not None:
                    print(f'\nThe next customer on the waitlist is: {name}, reservation time: {time}\n')
                else:
                    print(f'\nNo customers are on the waitlist\n')

            elif choice == "5":
                #TODO"""Print the waitlist"""
                reservation_list = self.waitlist.print_reservation_list()
                print('__________________________________________________\n')
                if reservation_list != []:
                    for name, time in reservation_list:
                        print(f'The next customer on the waitlist is: {name}, reservation time: {time}')
                else:
                    print(f'\nNo customers are on the waitlist\n')
                print('__________________________________________________\n')

            elif choice == "6":
                """exit the program at any time"""
                print("Thank you for using the Restaurant Reservation System!")
                break
            else:
                print("Invalid choice. Try again.")
    

s = Menu()
s.run()

