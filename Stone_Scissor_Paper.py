from Game import *
import random


Choosing_an_opponent = random.randint(1, 3)
Players_choice = int(input("Enter your choose: \n1 - Stone\n2 - Scissor\n3 - Paper\n------------------\n"))


invalid_input(Players_choice)
logic(Players_choice, Choosing_an_opponent)
show_opponents_answer(Choosing_an_opponent)

