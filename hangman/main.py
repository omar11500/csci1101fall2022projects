import re

# Get the answer.
answer = "What's up, Doc?"

answer = answer.upper()

# Pre-game setup.
answer_guessed = []

for current_answer_character in answer:
    if re.search("^[A-Z]$", current_answer_character):
        answer_guessed.append(False)
    else:
        answer_guessed.append(True)

# Game logic.
num_of_incorrect_guesses = 5

current_incorrect_guesses = 0

letters_guessed = []

# Let user play the game.
while current_incorrect_guesses < num_of_incorrect_guesses and False in answer_guessed:
    # Display game status.
    print(f"Number of incorrect guesses remaining: {num_of_incorrect_guesses - current_incorrect_guesses}")

    print("Letters guessed: ", end="")

    for current_letters_guessed in letters_guessed:
        print(current_letters_guessed, end=" ")

    print()

    # Display puzzle board.
    for current_answer_index in range(len(answer)):
        if answer_guessed[current_answer_index]:
            print(answer[current_answer_index], end="")
        else:
            print("_", end="")
    
    print()

    # Let the user guess a letter.
    letter = input("Enter a letter: ")

    # Check if user entered a valid letter.
    if 