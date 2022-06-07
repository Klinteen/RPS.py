import random

moves= ["R", "S", "P"]

#R for Rock
#S for Scissors
#P for paper

print("R FOR ROCK")
print("S FOR SCISSORS")
print("P FOR PAPER ")
print(" ")

while True:
    computer = random.choice(moves)
    player = input("Make your choice: R, S, P : ").upper()
    if player == computer:
        print("Player:", player, ":", "Computer:", computer)
        print("TIE! Play Again")
        print("")
    elif player == "R":
        if computer == "P":
            print("Player:", player, ":", "Computer:", computer)
            print("You Lose! Computer Win!")
            print("")
            break
        else:
            print("Player:", player, ":", "Computer:", computer)
            print("You Win!, Computer Lose!")
            print("")
            break
    elif player == "P":
        if computer == "S":
            print("Player:", player, ":", "Computer:", computer)
            print("You Lose! Computer Win!")
            print("")
            break
        else:
            print("Player:", player, ":", "Computer:", computer)
            print("You Win!, Computer Lose!")
            print("")
            break
    elif player == "S":
        if computer == "R":
            print("Player:", player, ":", "Computer:", computer)
            print("You Lose! Computer Win!")
            print("")
            break
        else:
            print("Player:", player, ":", "Computer:", computer)
            print("You Win!, Computer Lose!")
            print("")
            break

    else:
        print("Error! Try again")
        print("")




