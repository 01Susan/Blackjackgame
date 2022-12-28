from art import logo
import random
import os
from time import sleep

# Function to draw the random cards


def deal_card():
    """Gives an random card from list of cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Calculate if the player has got blackjack and replace 11 with 1 if sum of cards is over 21 and it also return sum of card"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, Opponent has a Blackjack"
    elif computer_score == 0:
        return "Win with a Blackjack"
    elif computer_score > 21:
        return "Opponet went over.You win"
    elif user_score > 21:
        return "You went over.You lose"
    elif user_score > computer_score:
        return "You Win"
    else:
        return "You Lose"


def playgame():
    user_card = []
    computer_card = []
    is_game_over = False

    print(logo)
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"    Your cards: {user_card}, current score: {user_score}")
        print(f"    Computer first card: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_dealing = input(
                "Type 'y' to get another card, type 'n' to pass: "
            ).lower()
            if user_dealing == "y":
                user_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"    Your final hand: {user_card},Final score {user_score}")
    print(f"    Your final hand: {computer_card},Final score {computer_score}")
    print(compare(user_score, computer_score))


playgame()
sleep(5)
os.system("cls")

while input("   Do you want to play the game again. Type 'y' or 'n'.").lower() == "y":
    playgame()
