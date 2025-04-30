# Wordle (Python Edition)

A simple command-line Wordle clone built in Python. This version includes difficulty settings, coloured feedback using `colorama`, and a dictionary lookup feature using a free API.

---

## Features

- 🎨 **Colour-coded feedback**:  
  - 🟩 Green: Correct letter in the correct position  
  - 🟨 Yellow: Correct letter in the wrong position  
  - ⬜ Grey: Incorrect letter  
- 📖 **Definition lookup**: Option to see the meaning of the answer word after the game ends  
- 🎯 **Difficulty modes**: Choose between EASY, NORMAL, and HARD (affects number of guesses)  
- 💡 **Hints**: One optional hint available mid-game  
- 🔠 **Letter bank**: See which letters you haven’t used yet

---

## Files

- `main_wordle.py`: The main script that runs the game loop  
- `game_functions.py`: Contains helper functions like feedback display, hint logic, and dictionary lookup  
- `answer_wordle_words.txt`: A list of possible answer words  
- `valid-wordle-words.txt`: A list of valid words the user can guess
- `main_wordle.exe`: Windows executable for running the game without Python

---

## Requirements

Install dependencies using:

```bash
pip install -r requirements.txt

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.