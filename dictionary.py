import random
from colorama import Fore, Back, Style
import requests
import json
import os
from pathlib import Path
import string
import time

# Tree Node Class
class TreeNode:
    def __init__(self, name, description=None):
        self.name = name            # Name of the action/choice
        self.description = description  # A short description of what this node represents
        self.children = []          # List of child nodes (subsequent actions/choices)

    def add_child(self, child_node):
        self.children.append(child_node)

    def display(self, level=0):
        # Display the node and its children (tree traversal)
        print(" " * (level * 2) + f"{self.name}: {self.description}")
        for child in self.children:
            child.display(level + 1)

# Setting the game parameters and initializing the tree
dirname = os.path.dirname(__file__)
os.chdir(dirname)
print("Current directory:", os.getcwd())

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

with open("valid-wordle-words.txt", "r") as valid_file:
    valid_words = valid_file.read()

if difficulty == 'EASY': 
    max_tries = 8
elif difficulty == 'HARD':
    max_tries = 4

# Create the tree structure for the game flow
root_node = TreeNode("Start", "Choose difficulty level and start the game")

difficulty_node = TreeNode("Difficulty Choice", "Select EASY, NORMAL, or HARD")
root_node.add_child(difficulty_node)

guess_node = TreeNode("Guess Word", "Make a guess and receive feedback")
difficulty_node.add_child(guess_node)

hint_node = TreeNode("Hint", "Option to get a hint (only at mid-game)")
guess_node.add_child(hint_node)

feedback_node = TreeNode("Feedback", "Display feedback after each guess")
guess_node.add_child(feedback_node)

# Define actions
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

def give_hint():
    for letter in answer:
        if letter in available_letters:
            print(f"Hint: The word contains the letter '{letter}'")
            break

# Game loop with tree traversal
start_time = time.time()
while tries < max_tries:
    start_time = time.time()
    guess = input('Enter a 5-letter word: ').upper()
    
    while len(guess) != word_length or guess not in valid_words.upper():
        if len(guess) != word_length:
            guess = input('That is not 5 letters, please Enter a 5-letter word: ').upper()
        elif guess not in valid_words.upper():
            guess = input('That is not a valid word, please Re-enter another 5-letter word: ').upper()
    
    tries += 1
    remaining_tries = (max_tries - tries)
    feedback()
    availability()

    if guess.upper() == answer.upper():
        end_time = time.time() - start_time
        print(f"You are correct, well done! It took you {tries} turns and {end_time} seconds to complete the Wordle")
        break

    if remaining_tries != 0:
        letter_bank = input("Would you like to see your available letters? Enter 'yes' or 'no': ").upper()
        if letter_bank == 'YES' or letter_bank == "Y":
            print("Available letters:", '  '.join(available_letters))
    
    if remaining_tries != 0:
        print(f'You have {remaining_tries} remaining tries')
    
    if tries == max_tries / 2:  # FLOAT
        hint = input("Would you like a hint? NOTE: this will be your last and final hint, if you decline you will not get another opportunity for a hint. Enter 'yes' or 'no': ").upper()
        if hint == 'YES' or hint == "Y":
            give_hint()

# Ask if the player wants to see the definition of the word
show_def = input(f"Would you like to see the definition of the answer word ({answer})? Enter 'yes' or 'no': ").upper()
if show_def == 'YES' or show_def == 'Y':
    get_definition()
else:
    quit()

# Display the tree of actions
root_node.display()
