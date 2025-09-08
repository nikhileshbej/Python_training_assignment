
class FlightNotFoundError(Exception):
    pass
class SeatsUnavailableError(Exception):
    pass
   
try:
    f = open('D:/Mindteck_Trainings/Python/Assignments/Hello/Exception_handling/FlifgtInfo.txt','r')
 
    try:
        data = f.read().split()
        flight_number, seats, price = data[0], int(data[1]), float(data[2])
 
        flightnumber_input = str(input("Enter flight number: "))
       
        if flightnumber_input != flight_number:
            raise FlightNotFoundError(f'Flight {flightnumber_input} does not exist!')
       
        tickets_required = int(input("Enter number of ticket to book: "))
        if tickets_required > seats:
          raise SeatsUnavailableError('Required number of seats not available!')
       
        total_cost = price * tickets_required
        discount = (total_cost / tickets_required) * 10 / 100
        print(f'Total Discounted: {discount}')
 
       
    except ValueError:
        print("Please enter valid input")
    except ZeroDivisionError:
        print("Please enter valid seat number")
   
except FileNotFoundError:
    print('File not found, please check the path')
 