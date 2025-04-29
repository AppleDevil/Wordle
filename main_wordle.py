import random 
import os
import string
import time
from game_functions import feedback, availability, get_definition, give_hint

def main():
    global guess, used_letters, available_letters, answer  # declare globals used in functions
    
    dirname = os.path.dirname(__file__)
    os.chdir(dirname)
    print("Current directory:", os.getcwd())

    # Visual separator
    separator = "-" * 60
    
    print(separator)
    difficulty = input("What difficulty would you like to play on, EASY, NORMAL, or HARD? ").upper()
    available_letters = list(string.ascii_uppercase)
    used_letters = []
    answer_words = []

    with open("answer_wordle_words.txt", "r") as answer_file:
        for line in answer_file:
            answer_words.append(line.strip())

    max_tries = 6
    word_length = 5
    tries = 0
    answer = random.choice(answer_words).upper()
    print(answer)
    with open("valid-wordle-words.txt", "r") as valid_file: 
        valid_words = valid_file.read()

    if difficulty == 'EASY': 
        max_tries = 8
    elif difficulty == 'HARD':
        max_tries = 4 

    print(separator)
    print("Welcome to my Wordle game, goodluck!")
    print(separator)
    
    start_time = time.time()
    while tries < max_tries:
        guess = input('Enter a 5 letter word: ').upper()
        while len(guess) != word_length or guess not in valid_words.upper():  
            if len(guess) != word_length:
                guess = input('That is not 5 letters, please Enter a 5 letter word: ').upper()
            elif guess not in valid_words.upper():
                guess = input('That is not a valid word, please Re-enter another 5 letter word: ').upper()
        tries += 1
        remaining_tries = (max_tries - tries)
        
        print(separator)
        print(f"Your guess: {guess}")
        feedback(guess, answer, used_letters)  # Call the function from game_functions
        availability(used_letters, available_letters)  # Call the function from game_functions
        
        if guess.upper() == answer.upper(): 
            end_time = time.time() - start_time
            print(separator)
            print(f"You are correct, well done! It took you {tries} turns and {round(end_time, 2)} seconds to complete the Wordle")
            print(separator)
            break
            
        if remaining_tries != 0:
            print(f'You have {remaining_tries} remaining tries')
            letter_bank = input("Would you like to see your available letters? Enter 'yes' or 'no': ").upper()
            if letter_bank == 'YES' or letter_bank == "Y":
                print("Available letters:", '  '.join(available_letters))
                
        if tries == max_tries / 2:
            print(separator)
            hint = input("Would you like a hint? NOTE: this will be your last and final hint. Enter 'yes' or 'no': ").upper()
            if hint == 'YES' or hint == "Y":
                give_hint(answer, available_letters)  # Call the function from game_functions
        
        # End of turn separator
        print(separator)

    if guess.upper() != answer.upper():
        print(separator)
        print(f"Bad luck! The word was '{answer}'. Better luck next time!")
        print(separator)

    show_def = input(f"Would you like to see the definition of the answer word ({answer})? Enter 'yes' or 'no': ").upper()
    if show_def == 'YES' or show_def == 'Y':
        print(separator)
        get_definition(answer)  # Call the function from game_functions
        print(separator)
    quit()

if __name__ == "__main__":
    main()