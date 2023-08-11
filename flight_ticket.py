Business_Class1 = [f'B{i}' for i in range(1, 7)]
Business_Class2 = [f'B{i}' for i in range(1, 7)]
Economy_Class1 = [f'E{i}' for i in range(7, 19)]
Economy_Class2 = [f'E{i}' for i in range(7, 19)]
B_cost = 2000
B_Meals = 200
E_cost = 1000
E_Meals = 100
Cancellation = 400
Booking_ID = 0
B_Available_seats1 = Business_Class1.copy()  # Move outside the while loop
B_Available_seats2 = Business_Class2.copy()
E_Available_seats1 = Economy_Class1.copy()
E_Available_seats2 = Economy_Class2.copy()
B_Booked_Seats1 = []
B_Booked_Meals1 = []
B_Booked_Seats2 = []
B_Booked_Meals2 = []
E_Booked_Seats1 = []
E_Booked_Meals1 = []
E_Booked_Seats2 = []
E_Booked_Meals2 = []

A = ""
B = ""
C = ""
D = ""
Total1 = 0
Total2 = 0
Total3 = 0
Total4 = 0
while True:
    Booking_ID += 1


    class Flight:
        def __init__(self, introduction, FlightNo, Class, Noseats, Meals, Select_seats):
            self.introduction = introduction
            self.Flightno = FlightNo
            self.Class = Class
            self.Noseats = Noseats
            self.Meals = Meals
            self.Select_seats = Select_seats


    introduction = int(input("Pls select (1) For Booking (2) Cancellation (3) Admin :"))
    if introduction == 1:
        FlightNo = int(input("Enter for Flight 101 for flight 102: "))
        Class = input("Enter the class type: Business/Economy: ").lower()
        Noseats = int(input("Please enter the number of seats you want: "))
        Meals = input("Please specify if you want to book meals along with the ticket (Yes/No): ").lower()
        if FlightNo == 101:
            if Class == "business":
                A = str(Booking_ID) + str(FlightNo) + "business"
                if len(B_Booked_Seats1) + Noseats <= 6:
                    for i in range(Noseats):
                        print("Available seats:", B_Available_seats1)
                        Select_seats = input("Select a seat: ").capitalize()
                        B_Available_seats1.remove(Select_seats)
                        B_Booked_Seats1.append(Select_seats)
                    if Meals == "yes":
                        B_Booked_Meals1 = B_Booked_Seats1.copy()
                        if len(B_Booked_Seats1) < 0:
                            Total1 = 0
                        else:
                            Total1 = Noseats * B_cost + Noseats * B_Meals
                            print("*" * 50)
                            print(f'Booking_ID: {Booking_ID}')
                            print(f'Flight No: {FlightNo}')
                            print(f'Business: {B_Booked_Seats1}')
                            print(f'Meals: {Meals}')
                            print(f'Total Cost: {Total1}')
                            print("*" * 50)
                    else:
                        if len(B_Booked_Seats1) < 0:
                            Total1 = 0
                        else:
                            Total1 = Noseats * B_cost
                            print("*" * 50)
                            print(f'Booking_ID: {Booking_ID}')
                            print(f'Flight No: {FlightNo}')
                            print(f'Business: {B_Booked_Seats1}')
                            print(f'Meals: {Meals}')
                            print(f'Total Cost: {Total1}')
                            print("*" * 50)
                else:
                    print("Business class for Flight No 101 is full consieder Economy class ")

            if Class == "economy":
                B = str(Booking_ID) + str(FlightNo) + "economy"
                if len(E_Booked_Seats1) + Noseats <= 12:
                    for i in range(Noseats):
                        print("Available seats:", E_Available_seats1)
                        Select_seats = input("Select a seat: ").capitalize()
                        E_Available_seats1.remove(Select_seats)
                        E_Booked_Seats1.append(Select_seats)

                    if Meals == "yes":
                        E_Booked_Meals1 = E_Booked_Seats1.copy()
                        if len(E_Booked_Seats1) < 0:
                            Total2 = 0
                        else:
                            Total2 = Noseats * E_cost + Noseats * E_Meals
                            print("*" * 50)
                            print(f'Booking_ID: {Booking_ID}')
                            print(f'Flight No: {FlightNo}')
                            print(f'Economy: {E_Booked_Seats1}')
                            print(f'Meals: {Meals}')
                            print(f'Total Cost: {Total2}')
                            print("*" * 50)
                    else:
                        if len(E_Booked_Seats1) < 0:
                            Total2 = 0
                        else:
                            Total2 = Noseats * E_cost
                            print("*" * 50)
                            print(f'Booking_ID: {Booking_ID}')
                            print(f'Flight No: {FlightNo}')
                            print(f'Economy: {E_Booked_Seats1}')
                            print(f'Meals: {Meals}')
                            print(f'Total Cost: {Total2}')
                            print("*" * 50)
                else:
                    print("Economy class of flight No 101 is full consider business class")

        if FlightNo == 102:
            if Class == "business":
                C = str(Booking_ID) + str(FlightNo) + "business"
                if len(B_Booked_Seats2) + Noseats <= 6:
                    for i in range(Noseats):
                        print("Available seats:", B_Available_seats2)
                        Select_seats = input("Select a seat: ").capitalize()
                        B_Available_seats2.remove(Select_seats)
                        B_Booked_Seats2.append(Select_seats)
                    if Meals == "yes":
                        B_Booked_Meals2 = B_Booked_Seats2.copy()
                        if len(B_Booked_Seats2) < 0:
                            Total3 = 0
                        else:
                            Total3 = Noseats * B_cost + Noseats * B_Meals
                            print("*" * 50)
                            print(f'Booking_ID: {Booking_ID}')
                            print(f'Flight No: {FlightNo}')
                            print(f'Business: {B_Booked_Seats2}')
                            print(f'Meals: {Meals}')
                            print(f'Total Cost: {Total3}')
                            print("*" * 50)
                    else:
                        if len(B_Booked_Seats2) < 0:
                            Total3 = 0
                        else:
                            Total3 = Noseats * B_cost
                            print("*" * 50)
                            print(f'Booking_ID: {Booking_ID}')
                            print(f'Flight No: {FlightNo}')
                            print(f'Business: {B_Booked_Seats2}')
                            print(f'Meals: {Meals}')
                            print(f'Total Cost: {Total3}')
                            print("*" * 50)
                else:
                    print("Business class of flight 102 is Full consider Economy ")

            if Class == "economy":
                D = str(Booking_ID) + str(FlightNo) + "economy"
                if len(E_Booked_Seats2) + Noseats <= 12:
                    for i in range(Noseats):
                        print("Available seats:", E_Available_seats2)
                        Select_seats = input("Select a seat: ").capitalize()
                        E_Available_seats2.remove(Select_seats)
                        E_Booked_Seats2.append(Select_seats)
                    if Meals == "yes":
                        E_Booked_Meals2 = E_Booked_Seats2.copy()
                        if len(E_Booked_Seats2) < 0:
                            Total4 = 0
                        else:
                            Total4 = Noseats * E_cost + Noseats * E_Meals
                            print("*" * 50)
                            print(f'Booking_ID: {Booking_ID}')
                            print(f'Flight No: {FlightNo}')
                            print(f'Economy: {E_Booked_Seats2}')
                            print(f'Meals: {Meals}')
                            print(f'Total Cost: {Total4}')
                            print("*" * 50)
                    else:
                        if len(E_Booked_Seats2) < 0:
                            Total4 = 0
                        else:
                            Total4 = Noseats * E_cost
                            print("*" * 50)
                            print(f'Booking_ID: {Booking_ID}')
                            print(f'Flight No: {FlightNo}')
                            print(f'Economy: {E_Booked_Seats2}')
                            print(f'Meals: {Meals}')
                            print(f'Total Cost: {Total4}')
                            print("*" * 50)
                else:
                    print("Economy class of Flight No 102 is full consider Business class")

    if introduction == 2:
        Bookingid = int(input("Pls enter the Booking ID : "))
        flight = int(input("pls enter the flight No :"))
        Class = input("Pls enter the class :")
        Y = str(Bookingid) + str(flight) + Class
        if Y in A:
            print("*" * 50)
            print("Booking_ID:", Booking_ID)
            print("Flight No:", flight)
            print("Status :Cancelled")
            print("Cancellation Fee: ", Cancellation)
            print("Refundable Amount :", Total1 - Cancellation)
            print("*" * 50)
        elif Y in B:
            print("*" * 50)
            print("Booking_ID:", Booking_ID)
            print("Flight No:", flight)
            print("Status :Cancelled")
            print("Cancellation Fee: ", Cancellation)
            print("Refundable Amount :", Total2 - Cancellation)
            print("*" * 50)
        elif Y in C:
            print("*" * 50)
            print("Booking_ID:", Booking_ID)
            print("Flight No:", flight)
            print("Status :Cancelled")
            print("Cancellation Fee: ", Cancellation)
            print("Refundable Amount :", Total3 - Cancellation)
            print("*" * 50)
        elif Y in D:
            print("*" * 50)
            print("Booking_ID:", Booking_ID)
            print("Flight No:", flight)
            print("Status :Cancelled")
            print("Cancellation Fee: ", Cancellation)
            print("Refundable Amount :", Total4 - Cancellation)
            print("*" * 50)
    if introduction == 3:
        print("*" * 50)
        print("Summery for Flight Number 101")
        Available_seats = str(B_Available_seats1)[1:-1] + " ," + str(E_Available_seats1)[1:-1]
        Booked_seats = str(B_Booked_Seats1)[1:-1] + str(E_Booked_Seats1)[1:-1]
        Meals_Booked = str(B_Booked_Meals1)[1:-1] + str(E_Booked_Meals1)[1:-1]
        print("Meals Booked :", Meals_Booked)
        print("Seats Booked :", Booked_seats)
        Total = Total1 + Total2
        print("Total : ", Total)
        print("Available Seats :", Available_seats)
        print("*" * 50)

        print("*" * 50)
        print("Summery for Flight Number 101")
        Available_seats = str(B_Available_seats2)[1:-1] + " ," + str(E_Available_seats2)[1:-1]
        Booked_seats = str(B_Booked_Seats2)[1:-1] + str(E_Booked_Seats2)[1:-1]
        Meals_Booked = str(B_Booked_Meals2)[1:-1] + str(E_Booked_Meals2)[1:-1]
        print("Meals Booked :", Meals_Booked)
        print("Seats Booked :", Booked_seats)
        Total = Total3 + Total4
        print("Total : ", Total)
        print("Available Seats :", Available_seats)
        print("*" * 50)
        break
Flit = Flight(introduction, FlightNo, Class, Noseats, Meals, Select_seats)