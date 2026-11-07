# Multiplication
num = int(input("Please type in a number: "))

num_one = 1

while num_one <= num:
    num_two = 1
    while num_two <= num:
        print(f"{num_one} x {num_two} = {num_one * num_two}")
        num_two += 1
    num_one += 1

# First letters of words
sentence = str(input("Please type in a sentence:"))

sentence_length = len(sentence)
index = 0

print(sentence[0])

while index < sentence_length:
    if sentence[index] == " ":
        print(sentence[index+1])
    index += 1

# Factorial
num = int(input("Please type in a number: "))

factorial = 1
index = 1

while num > 0:
    factorial = 1
    index = 1
    while index <= num:
        factorial *= index
        index += 1
    print(f"The factorial of the number {num} is {factorial}")
    num = int(input("Please type in a number: "))

print("Thanks and bye!")

# Taking turns
num = int(input("Please type in a number: "))

start = 1
end = num

while start <= end:
    print(start)
    if start != end:
        print(end)

    start += 1
    end -= 1