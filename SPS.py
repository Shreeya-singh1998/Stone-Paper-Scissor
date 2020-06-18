
from random import randint

#create list of options to play:
x = ["stone","paper", "scissor"]

#assign computer a random play:
computer = x[randint(0,2)]

#initialize player as false:
player = False

while player == False:
    player = input("stone, paper, scissor")
    if player == computer:
        print("It's a TIE!")
    elif player=="stone":
        if computer=="paper":
            print("Oops, You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player=="paper":
        if computer=="scissor":
            print("Oops, you lose!", computer, "cuts", player)
        else:
            print("You win!", player, "covers", computer)
    elif player=="scissor":
        if computer=="stone":
            print("Oops, you lose!", computer, "smashes", player)
        else:
            print("You win!", player, "cuts", computer)

    else:
        print("wrong entry, please enter a valid spelling.")

#player was set as true, but to continue loop set it back to False:
    player == False
    computer = x[randint(0,2)]
