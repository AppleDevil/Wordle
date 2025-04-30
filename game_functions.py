#game_functions.py
# This project is licensed under the MIT License. See the LICENSE file for details.
# Importing necessary libraries
import random  # Random is used for generating random numbers or choosing random elements
from colorama import Fore, Back, Style  # Importing for coloured output in the terminal
import requests  # For making requests to external APIs
import string  # For working with strings 

# Function to provide feedback on the guess (colour-coded letters)
def feedback(guess, answer, used_letters):
    for i in range(len(guess)):  # Loop through each letter in the guess
        letter = guess[i]  
        if letter not in used_letters:  
            used_letters.append(letter)  # Add it to the used letters list

        if letter == answer[i]:  # If the guessed letter matches the answer at the same position
            print(Fore.GREEN + letter + Style.RESET_ALL, end=" ")  # Print it in green

        elif letter in answer:  # If the guessed letter is in the answer but not in the correct position
            print(Fore.YELLOW + letter + Style.RESET_ALL, end=" ")  # Print it in yellow 

        else:  # If the letter is not in the answer at all
            print("\033[90m" + letter + "\033[39m", end=" ")  # Print it in grey (incorrect letter)
    print()  # Print a new line after giving feedback

# Function to find and display the definition of the answer word
def get_definition(answer):
    url = (f'https://api.dictionaryapi.dev/api/v2/entries/en/{answer}')  # Build URL to fetch the word definition
    response = requests.get(url)  
    if response.status_code == 200:  # If the request is successful 
        data = response.json() 
        meanings = data[0]["meanings"]  # Extract the meanings from the response
        for meaning in meanings:  # Loop through each meaning
            part_of_speech = meaning["partOfSpeech"]  # Get the part of speech (e.g., noun, verb, etc.)
            for definition in meaning["definitions"]:  # Loop through the list of definitions
                
                print(f"- ({part_of_speech}) {definition['definition']}")
    else:  
        print(f"'{answer}' is not a valid English word.")  

# Function to give a hint (reveals one letter from the answer)
def give_hint(answer, available_letters):
    for letter in answer:  # Loop through each letter in the answer word
        if letter in available_letters:  # If the letter is still available to be guessed
            print(f"Hint: The word contains the letter '{letter}'")  
            break  

# Function to update the list of available letters based on used letters
def availability(used_letters, available_letters):
    for used in used_letters:  # Loop through each letter in the used letters list
        if used in available_letters:  
            available_letters.remove(used)  
