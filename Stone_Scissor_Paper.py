#from Game import *
import random


Choosing_an_opponent = random.randint(1, 3)
Players_choice = int(input("Enter your choose: \n1 - Stone\n2 - Scissor\n3 - Paper\n------------------\n"))
if Players_choice > 2 or Players_choice < 0:
    print("Error: Enter a valid value")




#def step(Players_choice, Choosing_an_opponent):
#    if Players_choice == Stone:

