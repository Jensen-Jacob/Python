#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

# print(logo)


def play():
    print("Welcome to the number guessing game!")
    number = random.randint(1, 100)
    game_over = False
    while True:
        try:
            difficulty = input(
                "Choose a difficulty: Type 'easy' or 'hard': ").lower()
            if difficulty != "easy" and difficulty != "hard":
                raise Exception("Invalid input!")
            else:
                break
        except Exception as e:
            print(f"An error ocurred: {e}, try again!")
    if difficulty == "easy":
        turns = 10
    else:
        turns = 5
    while not game_over:
        print(f"You have {turns} turns to guess the number.")
        while True:
            try:
                guess = int(input("Make a guess: "))
                if type(guess) == int:
                    break
            except:
                print("Invalid Input! Try again.")
        if guess < number:
            print("Too low.")
            turns -= 1
        elif guess > number:
            print("Too high.")
            turns -= 1
        else:
            print(f"You got it! The number was {number}.")
            game_over = True
        if turns == 0:
            print(f"Game over! The number was {number}.")
            game_over = True
    while True:
        try:
            play_again = input(
                "Would you like to play again? Type 'yes' or 'no': ").lower()
            if play_again != "yes" and play_again != "no":
                raise Exception(
                    "Please answer 'yes' to play again and 'no' to exit.")
            else:
                break
        except Exception as e:
            print(f"{e}")

    if play_again == "yes":
        play()
    else:
        print("Thankyou for playing!")


play()
