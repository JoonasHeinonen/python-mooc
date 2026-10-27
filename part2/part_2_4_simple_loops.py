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

