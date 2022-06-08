import sys
no_of_tries = 5
import csv

with open('database.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'\t{row["imie"]})

used_letters = []
user_word = []

def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes

def show_state_of_game():
    print()
    print(user_word)
    print("Number of tries left:", no_of_tries)
    print("Used Letters:", used_letters)
###

for _ in word:
    user_word.append("_")

while True:
    letter = input("Enter a letter:")
    used_letters.append(letter)

    found_indexes = find_indexes(word, letter)

    if len(found_indexes) == 0:
        print("There is not letter like this.")
        no_of_tries -= 1


        if no_of_tries == 0:
            print("Game Over :(")
            sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index] = letter

    if "".join(user_word) == word:
        print("NICE")
        sys.exit(0)

    show_state_of_game()