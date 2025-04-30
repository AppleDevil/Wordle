# main_wordle.py
# This project is licensed under the MIT License. See the LICENSE file for details.
# importing necessary libraries and files
import random 
import os
import string
import time
from game_functions import feedback, availability, get_definition, give_hint #This imports the functions listed from the file game_functions

# Change the current directory to the folder this script is in
def main():
    dirname = os.path.dirname(__file__)
    os.chdir(dirname)
    print("Current directory:", os.getcwd()) #prints the current directory for debugging, this linecan be removed

    # Declares a visual separator which will make the game more readable for the player
    separator = "-" * 60 #prints a dash (-) 60 times

    print(separator) #print the seperator

    # Adjust tries allowed based on chosen difficulty
    difficulty = input("What difficulty would you like to play on, EASY, NORMAL, or HARD? ").upper() #ask the user what difficulty they want to play on, and convert their answer to uppercase
    if difficulty == 'EASY': #Easier mode gives more guesses
        max_tries = 8
    elif difficulty == 'HARD': # Hard mode gives fewer guesses
        max_tries = 4 
    else: #default amount of guesses
        max_tries = 6
    
    available_letters = list(string.ascii_uppercase) #use the string library and generate a list of the uppercase alphabet
    used_letters = [] #prepare the variable to store a list, this initializes an empty list
    answer_words = [] 

#Obtained from https://gist.github.com/cfreshman/a03ef2cba789d8cf00c08f767e0fad7b, official Wordle Wordlist 
    with open("answer_wordle_words.txt", "r") as answer_file: #open the file, read it and then close it and save its contents as a varible named answer_file 
        for line in answer_file: #iterate through each line in answer_file
            answer_words.append(line.strip()) # Remove the newline and add it to the list

#Obtained from https://gist.github.com/cfreshman/cdcdf777450c5b5301e439061d29694c official Wordle Wordlist 
    word_length = 5 #declare the word length
    tries = 0 #Used as a counter for how many tries have been done yet
    answer = random.choice(answer_words).upper() #using the random library select a random answer
    with open("valid-wordle-words.txt", "r") as valid_file: 
        valid_words = valid_file.read().upper()


    print(separator) #print the seperator 
    print("Welcome to my Wordle game, goodluck!") #welcoming message 
    print(separator)
    
    start_time = time.time() #Start a timer to measure how long the player takes

    # Main gameplay loop: continue until out of tries or correct guess
    while tries < max_tries:
        # Input for a guess
        guess = input('Enter a 5 letter word: ').upper()
         # Validate guess length and check if the word is in the valid word list
        while len(guess) != word_length or guess not in valid_words.upper():  
            if len(guess) != word_length:
                guess = input('That is not 5 letters, please Enter a 5 letter word: ').upper()
            elif guess not in valid_words.upper():
                guess = input('That is not a valid word, please Re-enter another 5 letter word: ').upper()
        tries += 1 #add 1 to the tries variable which counts the number of attempts. 
        remaining_tries = (max_tries - tries) #calculate the remaining amount of tries that the user has 
        
        print(separator)
        print(f"Your guess: {guess}") #output the users guess back to them
        feedback(guess, answer, used_letters)  # Call the function from game_functions to provide coloured feedback 
        availability(used_letters, available_letters)  # Call the function from game_functions to ask if they want to see their letter bank 
        
        if guess.upper() == answer.upper(): #Check if the guess matches the answer
            end_time = time.time() - start_time #end the timer if the correct answer was entered 
            print(separator)
            print(f"You are correct, well done! It took you {tries} turns and {round(end_time, 2)} seconds to complete the Wordle") #print the exiting message 
            print(separator)
            break #leave the while loop 
            
        # If guesses remain, offer to display remaining letters
        if remaining_tries != 0: 
            print(f'You have {remaining_tries} remaining tries')
            letter_bank = input("Would you like to see your available letters? Enter 'yes' or 'no': ").upper()
            if letter_bank == 'YES' or letter_bank == "Y":
                print("Available letters:", '  '.join(available_letters)) # Display the remaining available letters, joined with spaces for readability
        
        # Offer a single hint at halfway point
        if tries == max_tries / 2:
            print(separator)
            hint = input("Would you like a hint? NOTE: this will be your last and final hint. Enter 'yes' or 'no': ").upper()
            if hint == 'YES' or hint == "Y":
                give_hint(answer, available_letters)  # Call the function from game_functions
        
        # End of turn separator
        print(separator)

    #Post-game: if player didn't guess correctly
    if guess.upper() != answer.upper(): 
        print(separator)
        print(f"Bad luck! The word was '{answer}'. Better luck next time!")
        print(separator)

    # Offer to show the definition of the answer word
    show_def = input(f"Would you like to see the definition of the answer word ({answer})? Enter 'yes' or 'no': ").upper()
    if show_def == 'YES' or show_def == 'Y':
        print(separator)
        get_definition(answer)  # Call the function from game_functions
        print(separator)

# Ensure main() runs only when this script is executed directly
if __name__ == "__main__":
    main()
