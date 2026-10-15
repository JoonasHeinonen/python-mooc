# Orwell.
year = int(input("Please type in a number: "))

if year == 1984:
    print("Orwell")

# Absolute value.
number = int(input("Please type in a number: "))
msg = "The absolute value of this number is "

if number < 0:
    print(msg + str(number * -1))
else:
    print(msg + str(number))

# Soup or no soup.
soup_price = 5.90
name = input("Please tell me your name: ")

if name == "Jerry":
    pass
else:
    soups = int(input("How many portions of soup? "))
    print(f"The total cost is {soup_price * soups}")
print("Next please!")

# Order of magnitude.
nums = [1000, 100, 10]

msg = "This number is smaller than "

num_input = int(input("Please type in a number: "))

if num_input < nums[0]:
    print(msg + str(nums[0]))
if num_input < nums[1]:
    print(msg + str(nums[1]))
if num_input < nums[2]:
    print(msg + str(nums[2]))

print("Thank you!")

# Calculator.
num_1 = int(input("Number 1: "))
num_2 = int(input("Number 2: "))
operation = input("Operation: ")

if operation == "add":
    print(f"{num_1} + {num_2} = {num_1 + num_2}")
if operation == "subtract":
    print(f"{num_1} - {num_2} = {num_1 - num_2}")
if operation == "multiply":
    print(f"{num_1} * {num_2} = {num_1 * num_2}")

# Temperatures.
temperature = float(input("Please type in a temperature (F): "))

temperature_converted = (temperature - 32) * 5 / 9
print(f"{temperature} degrees Fahrenheit equals {temperature_converted} degrees Celsius")

if (temperature_converted < 0):
    print("Brr! It's cold in here!")

# Daily wages.
hourly_wage = float(input("Hourly wage: "))
hours_worked = int(input("Hours worked: "))
week_day = str(input("Day of the week: "))

daily_wages = 0

if week_day == "Sunday":
    daily_wages = (hourly_wage * 2) * hours_worked
else:
    daily_wages = hourly_wage * hours_worked

print(f"Daily wages: {daily_wages} euros")

# Loyalty bonus
points = int(input("How many points are on your card? "))
if points < 100:
    points *= 1.1
    print("Your bonus is 10 %")
elif points >= 100:
    points *= 1.15
    print("Your bonus is 15 %")

print("You now have", points, "points")

# What to wear tomorrow.
temp = int(input("Temperature: "))
rain = input("Will it rain (yes/no): ")

print("Wear jeans and a T-shirt")

if temp < 21:
    print("I recommend a jumper as well")

if temp < 11:
    print("Take a jacket with you")

if temp < 6:
    print("Make it a warm coat, actually")
    print("I think gloves are in order")

if rain == "yes":
    print("Don't forget your umbrella!")

# Solving a quadratic equation.

# Let's take the square root of math-module in use
from math import sqrt

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5
a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))

x1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
x2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)

print(f"The roots are {x1} and {x2}")