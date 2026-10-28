# Shall we continue?
print("hi")

while True:
    greet = input("Shall we continue?")
    if greet == "no":
        break
    print("hi")

print("okay then")

# Input validation.
from math import sqrt

while True:
    num = float(input("Please type in a number: "))

    if num == 0:
        break
    elif num > 0:
        print(sqrt(num))
    else:
        print("Invalid number")

print("Exiting...")

# Fix the code: Countdown.
number = 5
print("Countdown!")
while True:
    print(number)
    number = number - 1
    if number < 1:
        break

print("Now!")

# Repeat password.
first_password = input(str("Password: "))
password_input = input(str("Repeat password:"))

while password_input != first_password:
    print("They do not match!")
    password_input = input(str("Repeat password:"))

print("User account created!")

# PIN and number of attempts.
attempts = int(1)
correct_pin = int(4321)

pin = int(input("PIN: "))

while pin != correct_pin:
    print("Wrong")
    attempts = attempts + 1
    pin = int(input("PIN: "))

if attempts == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempts} attempts")

# The next leap year
year = 1 + int(input("Year: "))
print(f"The next leap year after {year - 1} is ", end="")
while not ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
    year += 1
print(year)

# Story
story_words = []

word = str(input("Please type in a word: "))
story_words.append(word)

while True:
    word = input("Please type in a word: ")

    if word == story_words[-1]:
        break

    if word == "end":
        break

    story_words.append(word)

print(" ".join(story_words))

# Working with numbers
import statistics

num_list = []

print("Please type in integer numbers. Type in 0 to finish.")
num = int(input("Number: "))

while num != 0:
    num_list.append(num)
    num = int(input("Number: "))

def count_vals(nums):
    print(f"Numbers typed in {len(nums)}")

def sum_vals(nums):
    print(f"The sum of the numbers is {sum(nums)}")

def mean_vals(nums):
    val = float(statistics.mean(nums))
    print(f"The mean of the numbers is {val}")

def pos_neg_vals(nums):
    neg_vals = 0
    pos_vals = 0

    for num in nums:
        if num < 0:
            neg_vals += 1
        elif num >= 1:
            pos_vals += 1
    
    print(f"Positive numbers {pos_vals}")
    print(f"Negative  numbers {neg_vals}")

def main(nums):
    count_vals(nums)
    sum_vals(nums)
    mean_vals(nums)
    pos_neg_vals(nums)

main(num_list)