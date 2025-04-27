#game_functions.py
import random
from colorama import Fore, Back, Style
import requests
import string

def feedback(guess, answer, used_letters):
    for i in range(len(guess)): 
        letter = guess[i]
        if letter not in used_letters:
            used_letters.append(letter)
        if letter == answer[i]:
            print(Fore.GREEN + letter + Style.RESET_ALL, end=" ")
        elif letter in answer:
            print(Fore.YELLOW + letter + Style.RESET_ALL, end=" ")
        else:
            print("\033[90m" + letter + "\033[39m", end=" ")
    print()  # prints a new line after giving the feedback

def availability(used_letters, available_letters):
    for used in used_letters:
        if used in available_letters:
            available_letters.remove(used)

def get_definition(answer):
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

def give_hint(answer, available_letters):
    for letter in answer:  
        if letter in available_letters:
            print(f"Hint: The word contains the letter '{letter}'")
            break
