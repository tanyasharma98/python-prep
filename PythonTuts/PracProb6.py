# ==============================================Guess The number=========================================
import random

a = int(input("Enter Minimum Range"))
b = int(input("Enter Maximum Range"))
list1 = []
i = 0
while i < 2:
    print(f"Player{i + 1}")
    random_number = random.randint(a, b)
    count = 0
    c = True
    while c:
        fop = int(input(f"Guess The Number in range{a}:{b}\n"))
        if fop < random_number:
            print(f"Your Guess {fop} is smaller than actual number.\n")
            count += 1
        elif fop > random_number:
            print(f"Your Guess {fop} is greater than actual number.\n")
            count += 1
        elif fop == random_number:
            count += 1
            i += 1
            print(f'Your Secret Number is {random_number}, you guessed correctly in {count}.\n')
            # Adding Both Player Count in List
            list1.append(count)
            c = False
# Now comparing Value of list with each Other to find the winner.
if int(list1[0]) < int(list1[1]):
    print(f"Player1 won the Game with {list1[0]} guesses.\n")
elif int(list1[0]) > int(list1[1]):
    print(f"Player2 won the Game with {list1[1]} guesses.\n")
else:
    print(f"Both player got same {list1[0]} guesses.")