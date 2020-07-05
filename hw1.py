import math
# Exercize1
#Shutting down program

def shut_down(s):
    if s == 'yes':
        # print("Shutting down")
        return "Shutting down"
    elif s == 'no':
        # print("Shutdown aborted")
        return 'Shutdown aborted'
    else:
        return ('Sorry')
        # print('Sorry')
# shut_down('yes')
# shut_down('no')
# shut_down(0)


# Exersize 2
# print(int(math.sqrt(100)))

def sqrt(value):
        number = math.sqrt(value)
        print(number)
# sqrt(13689)

# Exersize 3
def distance_from_zero(arg):
    if type(arg) == int or type(arg) == float:
        # return abs(arg)
        print(abs(arg))
    else:
        print('Nope')

# distance_from_zero('cat')
# distance_from_zero(-10)
# g = distance_from_zero(-20)
# print(g)

# Exersize 4

def hour():
    working_step = True
    while working_step:
        hour_total= raw_input('How many hours did you work?\n')
        try:
            hour_total = float(hour_total)
            working_step = False
            return hour_total
        except:
            print('enter a number')
def  rate():
    working_step = True
    while working_step:
        rate_total= raw_input('How many hours did you rate?\n')
        try:
            rate_total = float(rate_total)
            working_step = False
            return rate_total
        except:
            print('enter a number')

def computepay (hours, rate):
  if hours <= 40:
    pay = (hours * rate)
  else:
    pay = (40 * rate) + (hours-40)*rate*1.5
  return pay

# hours= hour()
# rates= rate()
# payment= computepay(hours, rates)

# Exersize 5
# Let's use functions to calculate your trip's costs:
# nights=raw_input("Enter nights:") vs. if you want to ask before
def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city == 'Charlotte':
        return 183
    if city == 'Tampa':
        return 220
    if city == 'Pittsburgh':
        return 222
    if city == 'Los Angeles':
        return 475

def rental_car_cost(days):
    # day = raw_input('Enter the city name\n')
    cost = days * 40
    if days >= 7:
        cost = cost -50
    elif days >= 3:
        cost =cost -20
    return cost


def trip_cost(city,days,nights):
    print(int(rental_car_cost(days) + plane_ride_cost(city) + hotel_cost(nights)))

# trip_cost('Charlotte',7,7)

# Exercise 6
# 3 ile bölünebilme
def cube(number):
    result = number*number*number
    return result
    print(result)

def by_three(number):
    if number %3 == 0:
        print(cube(number))
    else:
        print('returning False')
        return False

# by_three(19)
