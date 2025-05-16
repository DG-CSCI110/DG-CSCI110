#-------------------------------------------------------------------------------
# Name:        Hangman Final
# Purpose:     Final for Python
#
# Author:      DylanG
#
# Created:     05/14/2025
# Copyright:   (c) DylanG 2025
# Description: For my final, I chose to make a simple game of hangman.
# It will pick words from a list I created.
# Player score will be saved to a new txt file.
# The game will continue until player chooses to quit.
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

# For the list of words, I've picked some random words players found difficult to guess.
# For the rest I used a Random Word Generator to pick 50 words#

import random

# Word Load Function
def load_words(file_name="Hangman Words.txt"):
    """Load Words From File To List."""
    try:
        with open("Hangman Words.txt","r") as file:
            words = file.readlines()
            words = [word.strip() for word in words]
        return words
    except FileNotFoundError:
        print("Sorry Word Not Found!")
        return[]

# Random Word Function
def get_random_word(word_list):
    """Choose Random Word From List"""
    return random.choice(word_list).lower()

# Display Current Game State Function
def display_game_state(word, guessed_letters, wrong_guesses):
    """Display Word With Blanks For Unguessed Letters And Show State Of Hangman."""
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    print(f"\nCurrent word: {display_word}")
    print(f"Wrong guesses: {','.join(wrong_guesses)}")
    print(f"Attempts Remaining: {6 - len(wrong_guesses)}")

#Check If Player Won Function
def check_win(word, guessed_letters):
    """Check If Player Guessed Word Correctly."""
    return all(letter in guessed_letters for letter in word)

#Display Hangman Figure in ASCII Art Function
def display_hangman(wrong_guesses):
    """Hangman Figure Displayed Based On Number Of Wrong Guesses."""
    hangman_states = [
        """
        ----
        |  |
           |
           |
           |
        ----""",
        """
        ----
        |  |
        o  |
           |
           |
        ----""",
        """
        ----
        |  |
        o  |
        |  |
           |
        ----""",
        """
        ----
        |  |
        o  |
       /|  |
           |
        ----""",
        """
        ----
        |  |
        o  |
       /|\ |
           |
        ----""",
        """
        ----
        |  |
        o  |
       /|\ |
       /   |
        ----""",
        """
        ----
        |  |
        o  |
       /|\ |
       / \ |
        ----"""
        ]
    print(hangman_states[len(wrong_guesses)])

#Game Play Function
def play_game():
    """Play Hangman Game."""
    word_list = load_words()
    if not word_list:
        return

    word = get_random_word(word_list)
    guessed_letters = set()
    wrong_guesses = []
    score = 0

    while True:
        display_game_state(word, guessed_letters, wrong_guesses)
        display_hangman(wrong_guesses)

        guess = input("\nGuess Any Letter ('Quit' To Exit): ").lower()

        if guess == "quit":
            print("Thanks For Playing!!!")
            save_progress(score) # Score Is Saved When Player Quits
            break

        if len(guess) != 1 or not guess.isalpha():
            print("Please Enter Valid Letter.")
            continue

        if guess in guessed_letters or guess in wrong_guesses:
            print("Letter Already Guessed. Choose Again.")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print(f"Good Guess! '{guess}' Is In The Word!")
        else:
            wrong_guesses.append(guess)
            score -= 5  # Subtracts 5 points when guess is incorrect.
            print(f"Sorry, {guess} Is Wrong. Try Again.")

        if check_win(word, guessed_letters):
            print(f"\nCongratulations! You Guessed {word}!")
            save_progress(score) # Score Is Saved When Player Quits
            break
        if len(wrong_guesses) == 6:
            print(f"\nHangman! GAME OVER! The Word was: {word}")
            save_progress(score) # Score Is Saved When Player Quits
            break

# Save Player Score To Seperate TXT File Function
def save_progress(filename="Player_Score.txt", score=0):
    """Save Player Score To A Text File."""
    try:
        with open(filename, 'a') as file:
            file.write(f"Player Score: {score}\n")
        print(f"Score Saved!")
    except Exception as e:
        print(f"Error: {e}")

# This Runs The Game
if __name__ == "__main__":
    play_game()