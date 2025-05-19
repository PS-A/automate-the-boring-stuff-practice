# While/if testing.
"""
while True:
    print("Who are you?")
    name = input()
    if name != "PeePa":
        continue
    print("Hello, PeePa. What is the password? (It is a fish.)")
    password = input()
    if password == "tuna":
        break
print("Access granted.") 
"""

# For loops testing.
"""
import random
for i in range(5):
    print(random.randint(1, 10))
"""

# Testing sys.exit way of closing a while loop.
"""
import sys

while True:
    print("Type exit to exit.")
    response = input()
    if response == "exit":
        sys.exit()
    print("You typed " + response + ".")
"""

# Guess the number game.
"""
import random
secretNumber = random.randint(1, 10)
print("I am thinking of a number between 1 and 10.")

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print("Take a guess.")
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break

if guess == secretNumber:
    print("Good job! You guessed my number in " + str(guessesTaken) + " guesses!")
else:
    print("Nope. The number I was thinking of was " + str(secretNumber))
"""

# Rock, paper, scissors-game.
import random, sys

print("ROCK, PAPER, SCISSORS")

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True: # The main game loop.
    print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))
    while True: # The player input loop.
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        playerMove = input()
        if playerMove == "q":
            sys.exit() # Quit the program.
        if playerMove == "r" or playerMove == "p" or playerMove == "s":
            break # Break out of the player input loop.
        print("Type one of r, p, s, or q.")

    # Display what the player chose:
    if playerMove == "r":
        print("ROCK versus...")
    elif playerMove == "p":
        print("PAPER versus...")
    elif playerMove == "s":
        print("SCISSORS versus...")

    # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = "r"
        print("ROCK")
    elif randomNumber == 2:
        computerMove = "p"
        print("PAPER")
    elif randomNumber == 3:
        computerMove = "s"
        print("SCISSORS")

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print("It is a tie!")
        ties = ties + 1
    elif playerMove == "r" and computerMove == "s":
        print("You win!")
        wins = wins + 1
    elif playerMove == "p" and computerMove == "r":
        print("You win!")
        wins = wins + 1
    elif playerMove == "s" and computerMove == "p":
        print("You win!")
        wins = wins + 1
    elif playerMove == "r" and computerMove == "p":
        print("You lose!")
        losses = losses + 1
    elif playerMove == "p" and computerMove == "s":
        print("You lose!")
        losses = losses + 1
    elif playerMove == "s" and computerMove == "r":
        print("You lose!")
        losses = losses + 1