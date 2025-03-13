from random import *
import time
list_of_choice = ["R", "P","S"]

bot_score = 0
player_score = 0

user_choice = ""
bot_choice = ""
print("*ROCK*PAPER***SCCISORS***Lizard***Spock(M)\n")

while True:

    user_choice = input("Choice R,P,S,L,M-")
    bot_choice = choice(list_of_choice)

    print("And winner issss......\n")
    time.sleep(2)
    if user_choice == bot_choice:
        print("DRAW :(")

    elif user_choice == "R" and bot_choice == "P":
        print("BOT WINNER")
        bot_score += 1
        print(f"Player - {player_score} : {bot_score} - Bot")

    elif user_choice == "R" and bot_choice == "S":
        print("Player WINNER")
        player_score += 1
        print(f"Player - {player_score} : {bot_score} - Bot")

    elif user_choice == "P" and bot_choice == "R":
        print("Player WINNER")
        player_score += 1
        print(f"Player - {player_score} : {bot_score} - Bot")

    elif user_choice == "P" and bot_choice == "S":
        print("BOT WINNER")
        bot_score += 1
        print(f"Player - {player_score} : {bot_score} - Bot")

    elif user_choice == "S" and bot_choice == "R":
        print("BOT WINNER")
        bot_score += 1
        print(f"Player - {player_score} : {bot_score} - Bot")

    elif user_choice == "S" and bot_choice == "P":
        print("Player WINNER")
        player_score += 1
        print(f"Player - {player_score} : {bot_score} - Bot")

    elif user_choice == "L" and bot_choice == "P":
        print("Player WINNER")
        player_score += 1
        print(f"Player - {player_score} : {bot_score} - Bot")

    elif user_choice == "L" and bot_choice == "R":
        print("BOT WINNER")
        bot_score += 1
        print(f"Player - {player_score} : {bot_score} - Bot")

    elif user_choice == "L" and bot_choice == "M":
        print("Player WINNER")
        player_score += 1
        print(f"Player - {player_score} : {bot_score} - Bot")

    elif user_choice == "L" and bot_choice == "S":
        print("BOT WINNER")
        bot_score += 1
        print(f"Player - {player_score} : {bot_score} - Bot")

    elif user_choice == "M" and bot_choice == "S":
        print("Player WINNER")
        player_score += 1
        print(f"Player - {player_score} : {bot_score} - Bot")

    elif user_choice == "R" and bot_choice == "M":
        print("BOT WINNER")
        bot_score += 1
        print(f"Player - {player_score} : {bot_score} - Bot")

    elif user_choice == "M" and bot_choice == "L":
        print("BOT WINNER")
        bot_score += 1
        print(f"Player - {player_score} : {bot_score} - Bot")

    elif user_choice == "P" and bot_choice == "M":
        print("Player WINNER")
        player_score += 1
        print(f"Player - {player_score} : {bot_score} - Bot")

