from art import logo, vs
from game_data import data
import random
import os
import sys


def start_game():
  """Prints logo and asks user if they want to play the game"""
  print(logo)
  while True:
    play_game = input("Start game? Type 'y' for yes and 'n' for no: ")
    if play_game == "y" or play_game == "n":
      break
    else:
      print("Please type 'y' or 'n'\n")
  if play_game == "y":
    return True

def clear():
  """Clears the console"""
  # for windows, the command below would be os.system('cls')
  # I have written clear here because replit runs on linux
  os.system('clear')

def set_account(data):
  return data[random.randint(0, len(data) - 1)]

def format_data(account):
  """Formats the account data and results it in a printable format"""
  account_name = account['name']
  account_desc = account['description']
  account_country = account['country']
  return f"{account_name}, {account_desc} from {account_country}"

def get_input(account_one, account_two):
  """Gets user to provide a choice on which account has more followers"""
  while True:
    user_input = input(
      f"\n\nWho has more followers? Type 'A' for {account_one['name']} or 'B' for {account_two['name']}: "
    ).lower()
    if user_input != "a" and user_input != "b":
      print("Invalid input, please try again!")
    else:
      break
  return user_input

def check_answer(first_account, second_account, points, game_over):
  """Compares the followers of the first and second account and returns score, sets new second account and returns appropriate game_over boolean value"""
  if first_account["follower_count"] > second_account["follower_count"]:
    print(
      f"\nYou are right! {first_account['name']} has more followers than {second_account['name']}."
    )
    points += 1
    print(f"Your score: {points}")
    second_account = set_account(data)
  else:
    print(
      f"\nYou are wrong! {first_account['name']} has less followers than {second_account['name']}."
    )
    print(f"Your score: {points}")
    game_over = True

  return [points, game_over, first_account, second_account]

def play():
  game_over = False
  account_one = set_account(data)
  account_two = set_account(data)
  points = 0

  # Check whether game should start
  if not start_game():
    return

  # Loop for as long as the game is not over
  while not game_over:
    clear()
    
    # Display logo art
    print(logo)

    # Print first account data
    print(format_data(account_one))

    # Print vs art
    print(f"\n{vs}\n")

    # Print second account data
    print(format_data(account_two))

    # Obtain user input
    user_answer = get_input(account_one, account_two)

    # Check user input
    if user_answer == "a":
      # User chose first account
      points, game_over, account_one, account_two = check_answer(account_one, account_two, points, game_over)
    else:
      # User chose second account
      points, game_over, account_one, account_two = check_answer(account_two, account_one, points, game_over)

    # If user guessed right, check if they want to continue playing
    if not game_over:
      while True:
        continue_game = input(
          "Do you want to continue? Type 'y' for yes and 'n' for no: ")
        if continue_game == "y" or continue_game == "n":
          if continue_game == "y":
            break
          else:
            return
        else:
          print("Please type 'y' or 'n'\n")

  # If user doesnt want to continue playing/game is over, print:
  print("Game over, thankyou for playing!")
  sys.exit()

play()
