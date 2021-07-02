def invalid_input(Players_choice):
    if Players_choice > 3 or Players_choice < 1:
        exit("Error: Enter a valid value")


def logic(Players_choice, Choosing_an_opponent):
    if Players_choice == Choosing_an_opponent:
        print("Draw! :|")
    elif Players_choice == 3 and Choosing_an_opponent == 1:
        print("You won! :)")
    elif Players_choice < Choosing_an_opponent:
        print("You won! :)")
    else:
        print("You lose :(")


def show_opponents_answer(Choosing_an_opponent):
    if Choosing_an_opponent == 1:
        print("The opponent chose is Stone")
    elif Choosing_an_opponent == 2:
        print("The opponent chose is Scissors")
    elif Choosing_an_opponent == 3:
        print("The opponent chose is Paper")