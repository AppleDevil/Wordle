import random 
import termcolor
from colorama import Fore, Back, Style
import requests
import json
import os
from pathlib import Path
import string

dirname = os.path.dirname(__file__)
os.chdir(dirname)
print("Current directory:", os.getcwd())

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

def feedback():
    for i in range(len(guess)): 
        letter = guess[i]
        if letter not in used_letters:
            used_letters.append(letter) 
        if guess[i] == answer[i]:
            print(Fore.GREEN + guess[i] + Style.RESET_ALL, end=" ")
        elif guess[i] in answer:
            print(Fore.YELLOW + guess[i] + Style.RESET_ALL, end=" ")
        elif guess[i] not in answer:
            print("\033[90m" + guess[i] + "\033[39m", end=" ")
    print()

def availability():
    for used in used_letters:
        if used in available_letters:
           available_letters.remove(used)

def get_definition():
    url = (f'https://api.dictionaryapi.dev/api/v2/entries/en/{answer}')
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        meanings = data[0]["meanings"]
        for meaning in meanings:
            part_of_speech = meaning["partOfSpeech"]
            for definition in meaning["definitions"]:
                print(f"- ({part_of_speech}) {definition['definition']}")
    else:
        print(f"'{answer}' is not a valid English word.")   

def give_hint(): #we want the hint to be in the answer and not have been used yet 
    for letter in answer:  
        if letter in available_letters:
            print(f"Hint: The word contains the letter '{letter}'")
            break

while tries < max_tries:
    guess = input('Enter a 5 letter word: ').upper()
    while len(guess) != word_length:       #NOTE FIX THIS , WHEN IT PASSES THIS CHECK IT WONT COME BACK TO IT AGAIN AND INSTEAD ITLL SAY NOT A VALID WORD 
        guess = input('That is not 5 letters, please Enter a 5 letter word: ').upper()
    while guess not in valid_words.upper():
        guess = input('That is not a valid word, please Re-enter another 5 letter word: ').upper()
    tries +=  1
    remaining_tries = (max_tries - tries)
    availability()
    if guess.upper() == answer.upper():
        print("You are correct, well done!")
        break
    feedback()
    if remaining_tries != 1:
        letter_bank = input("would you like to see your available letters? Enter 'yes' or 'no': ").upper()
        if letter_bank== 'YES' or letter_bank == "Y":
            print(available_letters)
    if remaining_tries != 0:
        print(f'you have {remaining_tries} remaining tries')
    if tries == 3:
        hint = input("Would you like a hint? NOTE: this will be your last and final hint, if you decline you will not get another opportinity for a hint. Enter 'yes' or 'no': ").upper()
        if hint == 'YES' or hint == "Y":
            give_hint()

show_def = input(f"Would you like to see the definition of the answer word ({answer})? Enter 'yes' or 'no': ").upper()
if show_def == 'YES' or show_def == 'Y':
    get_definition()
else:
    quit()