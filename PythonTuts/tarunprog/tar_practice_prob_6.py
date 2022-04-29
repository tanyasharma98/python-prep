# import random
# b = int(input("Enter number 1"))
# c = int(input("Enter number 2"))
# a = random.randint(b, c)
#
#
# def players(player):
#     guess = 1
#     while True:
#         # player1 = int(input(f"Player Guess number between"))
#         if player != a:
#             guess += 1
#             if player < a:
#                 print("Guess a Bigger number")
#             else:
#                 print("Guess a Smaller number")
#             player = int(input(f"Guess number"))
#             continue
#             # print(f"Your guess is correct in {guess1} ")
#         else:
#             print(guess)
#             break
#     # print("Next player turn")
#     return guess
#
#
# if __name__ == '__main__':
#     player1 = int(input(f"Player_1 Guess number between {b} - {c}"))
#     # nu_first = players(player1)
#     print(f"Number of guess by player1:- {players(player1)}")
#     player2 = int(input(f"Player_2 Guess number between"))
#     nu_second = players(player2)
#     print(f"Number of guess by player1:- {players(player2)}")
#     if players(player1) < players(player2):
#         print(f"Number of guess by player1:- {nu_first}")
#         print(f"Number of guess by player2:- {nu_second}\n")
#         print("Player_1 win")
#     else:
#         print(f"Number of guess by player2:- {nu_second}\n")
#         print(f"Number of guess by player1:- {nu_first}")
#         print("Player_2 win")

import random
a = int(input("Enter number 1"))
b = int(input("Enter number 2"))
c = random.randint(a, b)
lst = []
for i in range(1, 3):
    guess = 1
    while True:
        player = int(input(f"Player{i} Guess number between {a} - {b}"))
        if player != c:
            guess += 1
            if player < c:
                print(f"Player_{i} your guess {player} is Smaller than actual number")
            else:
                print(f"Player_{i} your guess {player} is Bigger than actual number")

        else:
            lst.append(guess)
            print("Next player turn\n")
            break

if lst[0] < lst[1]:
    print(f"Number of guess by Player_1 = {lst[0]}\nNumber of guess by Player_2 = {lst[1]}\nPlayer_1 win")
else:
    print(f"Number of guess by Player_1 = {lst[0]}\nNumber of guess by Player_2 = {lst[1]}\nPlayer_2 win")
