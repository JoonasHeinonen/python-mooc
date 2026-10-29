# Print numbers
min_num = 2
max_num = 30

x = min_num
print(x)

while x < max_num:
    x += 2
    print(x)

# Fix the code: Countdown
print("Are you ready?")
number = int(input("Please type in a number: "))
while number != 0:
    print(number)
    number -= 1
print("Now!")

# Numbers: Upper limit
upper_limit = int(input("Upper limit:"))
index = 1

while index != upper_limit:
    print(index)
    index += 1

# Powers of two
upper_limit = int(input("Upper limit:"))
index = 1

while index <= upper_limit:
    print(index)
    index *= 2

# Powers of base n
upper_limit = int(input("Upper limit:"))
base_limit = int(input("Base:"))
index = 1

while index <= upper_limit:
    print(index)
    index *= base_limit

# The sum of consecutive numbers, version 1
index = 1
total = 0
base_limit = int(input("Limit: "))

while total < base_limit:
    total += index
    index += 1

print(total)

# The sum of consecutive numbers, version 2
index = 1
total = 0
base_limit = int(input("Limit: "))

calculation_str = ""

while total < base_limit:
    if index != 1:
        calculation_str += " + " + str(index)
    else:
        calculation_str += str(index)
    total += index
    index += 1

print(f"The consecutive sum: {calculation_str} = {total}")