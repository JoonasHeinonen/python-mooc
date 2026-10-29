# String multiplied
word = str(input("Please type in a string:"))
amount = int(input("Please type in an amount:"))

print(word * amount)

# The longer string
word_1 = str(input("Please type in string 1:"))
word_2 = str(input("Please type in string 2:"))

word_1_len = len(word_1)
word_2_len = len(word_2)

if word_1_len == word_2_len:
    print("The strings are equally long")
elif word_1_len > word_2_len:
    print(f"{word_1} is longer")
elif word_2_len > word_1_len:
    print(f"{word_2} is longer")

# End to beginning
word = str(input("Please type in a string:"))

word_len = len(word)

while word_len > 0:
    print(word[word_len - 1])
    word_len -= 1

# Second and second to last characters
word = str(input("Please type in a string:"))

word_len = len(word)

second_character = word[1]
second_last_character = word[word_len - 2]

if second_character == second_last_character:
    print(f"The second and the second to last characters are {second_last_character}")
else:
    print("The second and the second to last characters are different")

# A line of hashes
width = int(input("Width:"))
hashes = ""
index = 0

while index < width:
    index += 1
    hashes += "#"

print(hashes)

# A rectangle of hashes
width = int(input("Width:"))
height = int(input("Height:"))

index_x = 0
index_y = 0

hashes = ""

while index_x < width:
    index_x += 1
    hashes += "#"

while index_y < height:
    index_y += 1
    print(hashes)

# Underlining
msg = str(input("Please type in a string:"))

while msg != "":
    print(msg)
    lines = 0
    underlines = ""
    while lines < len(msg):
        underlines += "-"
        lines += 1
    print(underlines)
    msg = str(input("Please type in a string:"))