# Seven Brothers
def seven_brothers():
    names = [
        "Aapo",
        "Eero",
        "Juhani",
        "Lauri",
        "Simeoni",
        "Timo",
        "Tuomas"
    ]
    for i, name in enumerate(names):
        print(name)

if __name__ == "__main__":
    seven_brothers()

# The first character
def first_character(text):
    print(text[0])

if __name__ == "__main__":
    first_character('python')
    first_character('yellow')
    first_character('tomorrow')
    first_character('heliotrope')
    first_character('open')
    first_character('night')

# Mean
def mean(num_one, num_two, num_three):
    print((num_one + num_two + num_three) / 3)

if __name__ == "__main__":
    mean(1, 2, 3)

# Print many times
def print_many_times(text, times):
    index = 0
    while index < times:
        print(text)
        index += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print_many_times("python", 5)

# A square of hashes
def hash_square(length):
    row_index = 0
    column_index = 0
    hash_row = ""

    while row_index < length:
        hash_row += "#"
        row_index += 1

    while column_index < length:
        print(hash_row)
        column_index += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)

# Chessboard
def chessboard(length):
    row_index = 0

    while row_index < length:
        column_index = 0
        num = 1 if row_index % 2 == 0 else 0
        hash_row = ""

        while column_index < length:
            hash_row += str(num)

            if num == 1:
                num = 0
            else:
                num = 1

            column_index += 1

        print(hash_row)
        row_index += 1

# Testing the function
if __name__ == "__main__":
    chessboard(5)

# A word squared
def squared(word, length):
    for row in range(length):
        for column in range(length):
            index = row * length + column
            print(word[index % len(word)], end="")
        print()

if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)