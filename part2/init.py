# Fix the program
number = int(input("Please type in a number: "))
if number > 100:
    print("The number was greater than one hundred")
    number -= 100
    print("Now its value has decreased by one hundred")
    print("Its value is now " + str(number))
print(str(number) + " must be my lucky number!")
print("Have a nice day!")

# Number of characters.
word = str(input("Please type in a word: "))
word_length = len(word)
if word_length > 1:
    print(f"There are {word_length} letters in the word {word}")
print("Thank you!")

# Typecasting.
temperature = float(input("Please type in a number: "))

print("Integer part: ", int(temperature))
print("Decimal part: ", temperature - int(temperature))