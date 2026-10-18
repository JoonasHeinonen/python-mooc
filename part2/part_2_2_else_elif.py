# Age of maturity.
age = int(input("How old are you? "))

if age >= 18:
    print("You are of age!")
else:
    print("You are not of age!")

# Greater than or equal to.
num_1 = int(input("Please type in the first number: "))
num_2 = int(input("Please type in another number: "))

if num_1 == num_2:
    print("The numbers are equal!")
elif num_1 >= num_2:
    print(f"The greater number was: {num_1}")
elif num_1 < num_2:
    print(f"The greater number was: {num_2}")
else:
    print("Something went wrong!")

# The elder.
print("Person 1:")
person_1_name = str(input("Name: "))
person_1_age = int(input("Age: "))

print("Person 2:")
person_2_name = str(input("Name: "))
person_2_age = int(input("Age: "))

if person_1_age == person_2_age:
    print(f"{person_1_name} and {person_2_name} are the same age")
elif person_1_age >= person_2_age:
    print(f"The The elder is {person_1_name}")
elif person_1_age < person_2_age:
    print(f"The The elder is {person_2_name}")
else:
    print("Something went wrong!")

# Alphabetically last.
word_1 = str(input("Name: "))
word_2 = str(input("Name: "))

if word_1 == word_2:
    print("You gave the same word twice.")
elif word_1 > word_2:
    print(f"{word_1} comes alphabetically last")
elif word_1 < word_2:
    print(f"{word_2} comes alphabetically last")
else:
    print("Something went wrong!")