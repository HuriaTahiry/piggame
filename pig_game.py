#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Huria Tahiry 
"""
import random





def play_one_turn_pig():
    goal_score = 0
    while True:
        roll = random.randint(1, 6)
        if roll ==1:
            goal_score = 0
            print("You rolled a 1. Your turn is over.")
        else:
            goal_score += roll
            print(f"You rolled  {roll}.")
            print(f'Your score is {goal_score}.')
            choice = input("(r)oll again? ")
            if choice.lower() != "r":
                break
    score = take_turn()
    print('You scored', goal_score)





def play_solitaire_pig():
    target_score = int(input('Target Score?'))
    target = 0
    while True:
        roll = random.randint(1, 6)
        if roll == 1:
            target = 0
            print('oink')
        else:
            target += roll
            if target >= target_score:
                print('you win!')
                break
            print(f"You rolled  {roll}.")
            print(f'Your score is {target}.')
            choice = input("(r)oll again? ")
            if choice.lower() != "r":
                break
    print('Solitaire Pig Time!')





def play_heads_up_pig():
    import random
    # Function for player 1
    def play1(score1):
        print("Player1:")
        roll = random.randint(1, 6)
        print(f" You rolled a {roll}")
        if roll == 1:
            print("Oink")
            score1 = 0
            print(f"Player 1's score: {score1}")
            print("x = 0")
            return 0
        else:
            print(f"Player 1's score: {score1 + roll}")
            return roll

    # Function for player 2
    def play2(score2):
        print("Player2:")
        roll = random.randint(1, 6)
        print(f" You rolled a {roll}")
        if roll == 1:
            print("Oink")
            score2 = 0
            print(f"Player 2's score: {score2}")
            return 0
        else:
            print(f"Player 2's score: {score2 + roll}")
            return roll

    # code
    target_score = int(input("Input the target score."))
    score1 = 0
    score2 = 0
    while score1 < target_score and score2 < target_score:
        x = play1(score1)
        if x == 0:
            score1 = 0
        else:
            score1 = score1 + x
            choice1 = input("(r)oll again?")
            while choice1 == "r" and score1 < target_score:
                x1 = play1(score1)
                score1 = score1 + x1
                choice1 = input("(r)oll again?")
                if score1 >= target_score:
                    print(f"Player 1 won. Your score is {score1}.")
            break;

        y = play2(score2)
        if y == 0:
            score2 = 0
        else:
            score2 = score2 + y
            choice2 = input("(r)oll again?")
            while choice2 == "r" and score2 < target_score:
                y1 = play2(score2)
                score2 = score2 + y1
                choice2 = input("(r)oll again?")
                if score2 >= target_score:
                    print(f"Player 2 won. Your score is {score2}.")
            break;

    # if score1 >= target_score:
    #   print(f"Player 1 won. Your score is {score1}.")
    # else:
    #   print(f"Player 2 won. Your score is {score2}.")

    # while True:
    #     print('new turn: Player2')
    #     roll = random.randint(1, 6)
    #     if roll == 1:
    #         print('oink')
    #         break
    #     scores2 += roll
    #     if scores2 >= target_score:
    #         print('player2 win!')
    #         break
    #     print(f"You rolled  {roll}.")
    #     print(f'Your score is {scores2}.')
    #     choice = input("(r)oll again? ")
    #     if choice.lower() != "r":
    #         break
    # roll2 = random.randint(1, 6)
    # if roll2 == 1:
    #     print('oink')
    #     break
    # else:
    #     scores2 += roll2
    #     scores2 >= target_score
    #     print('player2 win!')
    #     break
    #     print(f"You rolled  {roll2}.")
    #     print(f'Your score is {scores2}.')
    #     choice = input("(r)oll again? ")
    #     if choice.lower() != "r":
    #         break

    print('Heads-up Pig Time!')





def start():
    games = {
        't': ('1-Turn Pig', play_one_turn_pig),
        's': ('Solitaire Pig', play_solitaire_pig),
        'h': ('Heads-up Pig', play_heads_up_pig),
    }
    print('Menu\n----')
    for (key, game) in games.items():
        print(key, ": ", game[0], sep='')
    choice = input('\nGame choice: ')
    if choice in games:
        games[choice][1]()
    else:
        print('Sorry, that is not a game choice')


if __name__ == '__main__':
    start()
