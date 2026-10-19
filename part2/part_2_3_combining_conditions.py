# Nephews of Donald Duck and Mickey Mouse.
donald_nephews = ["Huey", "Dewey", "Louie"]
mickey_nephews = ["Morty", "Ferdie"]

donald_nephew_name_found = False
mickey_nephew_name_found = False

name = input("Please type in your name: ")

for nephew in donald_nephews:
    if name == nephew:
        donald_nephew_name_found = True

for nephew in mickey_nephews:
    if name == nephew:
        mickey_nephew_name_found = True

if donald_nephew_name_found:
    print("I think you might be one of Donald Duck's nephews.")
elif mickey_nephew_name_found:
    print("I think you might be one of Mickey Mouse's nephews.")
else:
    print("You're not a nephew of any character I know of.")

# Grades and points.
# Grades and points.
points = int(input("How many points [0-100]: "))

if points < 0 or points > 100:
    print("Grade: impossible!")
elif points < 50:
    print("Grade: fail")
elif points >= 50 and points <= 59:
    print("Grade: 1")
elif points >= 60 and points <= 69:
    print("Grade: 2")
elif points >= 70 and points <= 79:
    print("Grade: 3")
elif points >= 80 and points <= 89:
    print("Grade: 4")
elif points >= 90 and points <= 100:
    print("Grade: 5")
else:
    print("Something wrent wrong...")

# FizzBuzz.
num = int(input("Number"))
msg = ""

if num % 5 == 0:
    msg = "Buzz"
if num % 3 == 0:
    msg = "Fizz"
if num % 3 == 0 and num % 5 == 0:
    msg = "FizzBuzz"

print(f"{msg}")

# Leap year.
year = int(input("Please type in a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("That year is a leap year.")
        else:
            print("That is not a leap year.")
    else:
        print("That year is a leap year.")
else:
    print("That is not a leap year.")

# Alphabetically in the middle.
letter_one = str(input("1st letter: "))
letter_two = str(input("2nd letter: "))
letter_three = str(input("3rd letter: "))

if (letter_one < letter_two < letter_three
        or letter_three < letter_two < letter_one):
    print(f"The letter in the middle is {letter_two}")
elif (letter_two < letter_one < letter_three
        or letter_three < letter_one < letter_two):
    print(f"The letter in the middle is {letter_one}")
else:
    print(f"The letter in the middle is {letter_three}")

# Gift tax calculator.

value = int(input("Value of gift: "))

if value < 5000:
    print("No tax!")
elif value == 5000:
    print("Amount of tax: 100.0 euros")
elif value > 5000 and value < 25000:
    tax = (100 + (value - 5000) * 0.08)
    print(f"Amount of tax: {tax} euros")
elif value > 25000 and value < 55000:
    tax = (1700 + (value - 25000) * 0.10)
    print(f"Amount of tax: {tax} euros")
elif value > 55000 and value < 200000:
    tax = (4700 + (value - 55000) * 0.12)
    print(f"Amount of tax: {tax} euros")
# 200 000 — 1 000 000 (0.15)
# 1 000 000 — (0.17)
# 142 100
elif value > 200000 and value < 1000000:
    tax = (22100 + (value - 200000) * 0.15)
    print(f"Amount of tax: {tax} euros")
elif value > 1000000:
    tax = 142100 + (value - 1000000) * 0.17
    print(f"Amount of tax: {tax} euros")