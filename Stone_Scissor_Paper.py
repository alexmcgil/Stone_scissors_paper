import random


Choosing_an_opponent = random.randint(1, 3)
Players_choice = int(input("Enter your choose: \n1 - Stone\n2 - Scissor\n3 - Paper\n------------------\n"))


if Players_choice > 3 or Players_choice < 1:
    exit("Error: Enter a valid value")


if Players_choice == Choosing_an_opponent:
    print("Draw! :|")
elif Players_choice == 3 and Choosing_an_opponent == 1:
    print("You won! :)")
elif Players_choice < Choosing_an_opponent:
    print("You won! :)")
else:
    print("You lose :(")

if Choosing_an_opponent == 1:
    print("The opponent chose is Stone")
elif Choosing_an_opponent == 2:
    print("The opponent chose is Scissors")
elif Choosing_an_opponent == 3:
    print("The opponent chose is Paper")
