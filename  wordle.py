def get_guess():
    while True:
        guess = input("What word is this?: ")
        if len(guess) == 5:
            return guess.upper()
        print("Please enter a 5-letter word.")

def print_word(word):
    print(' '.join(word))

def exact_match_compare(solution, guess):
    result = ""
    for i in range(5):
        if solution[i] == guess[i]:
            result += "🟢"
        else:
            result += "🔴"
    return result

def one_turn(solution):
    guess = get_guess()  # Ask for player's guess
    print_word(guess)    # Display guess with spaces
    match = exact_match_compare(solution, guess)  # Compare and get result string
    print(match)         # Output result with emojis
    if guess == solution:
        print("Congratulations!")
        exit()

import random

def make_solution():
    words = [
        "WHICH", "THEIR", "THERE", "WOULD", "OTHER", "THESE",
        "ABOUT", "FIRST", "COULD", "AFTER"
    ]
    return random.choice(words)

soln = make_solution()        # Pick a random solution word
one_turn(soln)                # 1st attempt
one_turn(soln)                # 2nd attempt
one_turn(soln)                # 3rd attempt
one_turn(soln)                # 4th attempt
one_turn(soln)                # 5th attempt
one_turn(soln)                # 6th attempt
print(f'Word was "{soln}", better luck next time.')  # Shown if user didn’t win
