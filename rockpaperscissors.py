# Umar Azizi
# Rock, paper, scissors Game v1
# 6/18/2021

# I haven't yet coded for;
#   - invalid inputs
#   - replaying the game
#   - choice of different number of rounds

import random  # Importing the random thingy to get the computer to make choices

# initializing variables
rounds = 0
player = 0
computer = 0
my_wins = 0
comp_wins = 0
ties = 0
choices = ["rock", "paper", "scissors"]

print("Do you want play rock, paper, scissors?\n y or n")
start = input().casefold()  # to make sure uppercase letters don't cause an issue

if start == "y":  # If y is entered, the game begins
    print("Press Q to quit anytime, otherwise type your choice")

    while player != "q":
        print("\nRock, Paper, Scissors, SHOOT")
        player = input().casefold()  # to make sure uppercase letters don't cause an issue
        if player == "q":  # Players can quit whenever they want, thus ending the program
            print("\nokay quitter")
            break

        computer = random.choice(choices)  # Here the computer makes its choice and prints it
        print(computer)

        # All the possible scenarios, I could've grouped them better
        if player == "rock" and computer == "scissors":
            print("You win")  # The winner is pointed out
            my_wins += 1  # The win counter of the winner goes up by 1
        elif player == "rock" and computer == "paper":
            print("I win")
            comp_wins += 1
        elif player == "paper" and computer == "rock":
            print("You win")
            my_wins += 1
        elif player == "paper" and computer == "scissors":
            print("I win")
            comp_wins += 1
        elif player == "scissors" and computer == "rock":
            print("I win")
            comp_wins += 1
        elif player == "scissors" and computer == "paper":
            print("You win")
            my_wins += 1
        else:  # In case of ties
            print("Tie game")
            ties += 1

        rounds += 1  # After each turn the round counter goes up by 1
        if rounds == 3:  # Game ends after 3 rounds are done
            print()
            print("You won {} times".format(my_wins))
            print("I won {} times".format(comp_wins))
            print("There were {} ties\n".format(ties))

            # The message prints for each specific scenario
            if my_wins > comp_wins:
                print("You won the game, surprising")
            elif ties == 3 or my_wins == comp_wins == ties:
                print("Nobody won, hope you enjoyed wasting your time")
            else:
                print("I won the game, I am inevitable")
            break

else:  # If the player entered n instead of y at the start
    print("Log out of life then")
