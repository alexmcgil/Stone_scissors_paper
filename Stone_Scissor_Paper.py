from Game import *
import random


Choosing_an_opponent = random.randint(0, 2)
Players_choice = input("Enter your choose (Stone or Scissor or Paper):")
step(Players_choice)
