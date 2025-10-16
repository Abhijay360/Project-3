import random

def get_guess():
    while True:
        guess = input("What word is this?: ")
        if len(guess) == 5:
            return guess.upper()
        print("Please enter a 5-letter word.")

def print_word(word):
    print(' '.join(list(word)))

def exact_match_compare(solution, guess):
    result = ""
    for i in range(5):
        if solution[i] == guess[i]:
            result += "🟢"
        else:
            result += "🔴"
    return result

def one_turn(solution):
    guess = get_guess()
    print_word(guess)
    match = exact_match_compare(solution, guess)
    print(match)
    if guess == solution:
        print("Congratulations!")
        exit()

def make_solution():
    words = [
        "WHICH", "THEIR", "THERE", "WOULD", "OTHER", "THESE",
        "ABOUT", "FIRST", "COULD", "AFTER"
    ]
    return random.choice(words)

if __name__ == '__main__':
    soln = make_solution()
    one_turn(soln)
    one_turn(soln)
    one_turn(soln)
    one_turn(soln)
    one_turn(soln)
    one_turn(soln)
    print(f'Word was "{soln}", better luck next time.')

