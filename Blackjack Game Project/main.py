from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card():
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_score(player_score, computer_score):
    if player_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return f"Computer got blackjack! You Lose."
    elif player_score == 0:
        return f"You got blackjack! You Win."
    elif player_score > 21:
        return f"You went over. You Lose."
    elif computer_score > 21:
        return f"Computer went over. You Win!."
    elif player_score > computer_score:
        return f"You Win."
    else:
        return f"You Lose."      

def blackjack():
    play_choice = input("Do you want to play a game of Blackjack? Type 'y' for yes or 'n' for no: ")
    player_cards = []
    computer_cards = []
    player_score = 0
    computer_score = 0
    play_game = False
    is_game_over = False
    if play_choice == "y":
        play_game = True
    else:
        return
    while play_game:
        print(logo)
        for i in range(2):
            player_cards.append(draw_card())
            computer_cards.append(draw_card())
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        while not is_game_over:
            if player_score == 0 or computer_score == 0 or player_score > 21:
                is_game_over = True
            else:
                additional_card = input("Do you want to get another card? Type 'y' for yes or 'n' for no: ")
                if additional_card == "y":
                    player_cards.append(draw_card())
                    player_score = calculate_score(player_cards)
                    print(f"Your cards: {player_cards}, current score: {player_score}")
                    print(f"Computer's first card: {computer_cards[0]}")
                else:
                    is_game_over = True
            while computer_score != 0 and computer_score <= 16:
                computer_cards.append(draw_card())
                computer_score = calculate_score(computer_cards)
            if is_game_over:
                print(f"Your final hand: {player_cards}, your final score: {player_score}, computer's final hand: {computer_cards}, computer's final score: {computer_score}.")
                print("Result:", compare_score(player_score, computer_score))
                play_game = False
    blackjack()
        
blackjack()
        