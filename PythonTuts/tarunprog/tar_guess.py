# run this program
print("number of moves = 5")
i = 5
print("Welcome to mind hec")
try:
    def game(i):
        """The best game which never fails"""
        while i >= 1:
            a = int(input("Enter your number"))
            if a > 40:
                i = i - 1
                print("bad choice ,guess low", f"number of guess left{i}")
            elif a <= 40 and a > 18:
                i = i - 1
                print(f"ohhh guess little low number of guess left{i}")

            elif a < 18 and a >= 0:
                i = i - 1
                print(f"guess a little high chances lest {i}")
            else:
                print("you win")
                break
        print('better luck next time')
        if i == 0:
            print("game over")
            y = input("do you want to play again --Y/N")
            if y == "Y":
                i = 5
                game(i)
            else:
                print("see you")


    game(i)
except Exception as e:
    print(f"Enter valid number\n{e}")
