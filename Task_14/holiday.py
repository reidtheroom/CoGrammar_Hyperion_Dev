# calculate user's total holiday cost inc. plane, hotel and car-rental cost

# calculate the total cost of the hotel

def hotel_cost(num_nights):

    base_rate = 125

    total = base_rate * num_nights

    print(f"Hotel Cost: £{total}")

    return total

# calculate cost of flight

def plane_cost(city_flight):

    if city_flight == "Paris":
        total = 100
        print(f"Flight Cost: £{total}")
        return total
    
    elif city_flight == "Rome":
        total = 150
        print(f"Flight Cost: £{total}")
        return total
    
    elif city_flight == "New York":
        total = 400
        print(f"Flight Cost: £{total}")
        return total
    
    elif city_flight == "Dubai":
        total = 500
        print(f"Flight Cost: £{total}")
        return total
    
    else:
        total = 350
        print(f"Flight Cost: £{total}")
        return total
    
# calculate total cost of rental car
    
def car_rental(rental_days):

    standard_rate = 30

    total = standard_rate * rental_days

    print(f"Rental Car Cost: £{total}")

    return total

# calculate total holiday cost

def holiday_cost(hotel_cost, plane_cost, car_rental):

    total = hotel_cost + plane_cost + car_rental

    print(f"Total Holiday Cost: £{total}")


# get the city user is flying to

city_flight = input("What city are you flying to? ")

# number of hotel nights

num_nights = int(input("How many nights will you be staying in your hotel? "))

# days for a rental car

rental_days = int(input("How many days will you be hiring a car? "))

hotel = hotel_cost(num_nights)
plane = plane_cost(city_flight)
car = car_rental(rental_days)
holiday_cost(hotel, plane, car)

