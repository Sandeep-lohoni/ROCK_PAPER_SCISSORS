import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


playagain = True

while playagain:
    playerchoice = input(
        "\nEnter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2, or 3.")

    computerchoice = random.choice("123")
    computer = int(computerchoice)

    print("\nYou chose " + str(RPS(player)).replace('RPS.', '') + ".")
    print("Computer chose " + str(RPS(computer)).replace('RPS.', '') + ".")

    if player == 1 and computer == 3:
        print("🎉You win!")
    elif player == 2 and computer == 3:
        print("🎉You win!")
    elif player == 3 and computer == 2:
        print("🎉You win!")
    elif player == computer:
        print("😐Tie game!")
    else:
        print("🐍Computer wins!")

    playagain = input("\nPlay again? \nY for YES or \nQ to QUIT\n\n")

    if playagain.lower() == "y":
        continue
    else:
        print("\n🎉🎉🎉🎉")  
        print("Thankyou for playing!\n")  
        playagain = False

sys.exit("Bye!👋")




