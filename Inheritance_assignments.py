
# Create a base class Flight with basic flight information. Create a derived class ScheduledFlight that adds scheduling information.
 
# Requirements:
# -Flight should have attributes: flight number, airline.
# -ScheduledFlight should add departure time and arrival time.
# -Include methods to display complete flight information.

class FightInformation:
    def __init__(self, flight_number, airline):
        self.flight_number = flight_number
        self.airline = airline
    
class ScheduledFlight(FightInformation):
    def __init__(self, flight_number, airline, deparature_time, arrival_time):
        super().__init__(flight_number, airline)
        self.deparature_time = deparature_time
        self.arrival_time = arrival_time

    def display(self):
        print(f"Flight number: {self.flight_number}\nAirline: {self.airline}\nDeparature time: {self.deparature_time}\nArrival time: {self.arrival_time}")

# Create object 
sf = ScheduledFlight("AI101", "Air India", "10:00", "16:00")
sf.display()


# Create a base class Person, derived class CrewMember, and a further derived class Pilot.
# -Person contains name and ID.
# -CrewMember adds role (e.g., "Cabin Crew", "Pilot").
# -Pilot adds license number and rank (e.g., "Captain").
        
class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class CrewMember(Person):
    def __init__(self, name, id, role):
        super().__init__(name, id)
        self.role = role

class Pilot(CrewMember):
    def __init__(self, name, id, role, license_no, rank):
        super().__init__(name, id, role)
        self.license_no = license_no
        self.rank = rank

    def display(self):
         print(f"""
               Name: {self.name}
               ID: {self.id}
               Role: {self.role}
               License Number: {self.license_no}
               Rank:{self.rank}""")


pilot = Pilot("Ram", 101, "Pilot", 1001, "Midle")
print("############################")
pilot.display()



# Create one class PassengerDetails and another class TicketDetails. Create a new class Booking that inherits from both.
# Requirements:
# - PassengerDetails has name, age.
# - TicketDetails has ticket number, seat number.
# - Booking shows all information.
   
class PassengerDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class TicketDetails:
    def __init__(self, ticket_number, seat_number):
        self.ticket_number = ticket_number
        self.seat_number = seat_number

class Booking(PassengerDetails, TicketDetails):
    def __init__(self, name, age, ticket_number, seat_number):
        PassengerDetails.__init__(self, name, age)
        TicketDetails.__init__(self, ticket_number, seat_number)

    def disply_detsils(self):
            print(f"""Name: {self.name}
Age: {self.age}
Ticket Number: {self.ticket_number}
Seat Number: {self.seat_number}""")


            
booking = Booking("Naveen", 25, 101, 21)
print("############################")
booking.disply_detsils()





        
