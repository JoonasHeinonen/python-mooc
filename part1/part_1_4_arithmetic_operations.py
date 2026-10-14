# Times five.
num = input("Please type in a number: ")
num_times = int(num) * 5
print(f"{num} times 5 is {num_times}")

# Name and age.
name = input("What is your name? ")
year = input("Which year were you born? ")

age = 2021 - int(year)

print(f"Hi {name}, you will be {age} years old at the end of the year 2021")

# Seconds in a day.
days = input("How many days? ")
seconds = int(days) * 24 * 60 * 60
print(f"Seconds in that many days: {seconds}")

# Product.
number_1 = int(input("Please type in the first number: "))
number_2 = int(input("Please type in the second number: "))
number_3 = int(input("Please type in the third number: "))

product = number_1 * number_2 * number_3

print("The product is", product)

# Sum and product.
number_1 = int(input("Number 1: "))
number_2 = int(input("Number 2: "))

print(f"The sum of the numbers: {number_1 + number_2}")
print(f"The product of the numbers: {number_1 * number_2}")

# Sum and mean.
number_1 = int(input("Number 1: "))
number_2 = int(input("Number 2: "))
number_3 = int(input("Number 3: "))
number_4 = int(input("Number 4: "))

numbers_sum = number_1 + number_2 + number_3 + number_4
numbers_mean = numbers_sum / 4
print(f"The sum of the numbers is {numbers_sum} and the mean is {numbers_mean}")

# Food expenditure.
times_eaten = int(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
money_spent = float(input("How much money do you spend on groceries in a week? "))

cafeteria_costs = price * times_eaten
weekly_costs = money_spent + cafeteria_costs
daily_costs = weekly_costs / 7

print("Average food expenditure:")
print(f"Daily: {daily_costs} euros")
print(f"Weekly: {weekly_costs} euros")

# Students in groups.
# Write your solution here
students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))

groups = (students + group_size - 1) // group_size

print(f"Number of groups formed: {groups}")