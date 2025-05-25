# Input cat names to a list and print it.
"""
catNames = []
while True:
    print("Enter the name of cat " + str(len(catNames) + 1) +
      " (Or enter nothing to stop.):")
    name = input()
    if name == "":
        break
    catNames = catNames + [name]  # list concatenation
print("The cat names are:")
for name in catNames:
    print("  " + name)
"""

# In/Not in testing.
"""
myPets = ["Zophie", "Pooka", "Fat-tail"]
print("Enter a pet name:")
name = input()
if name not in myPets:
    print("I do not have a pet named " + name)
else:
    print(name + " is my pet.")
"""

# Magic 8 ball with a list.
"""
import random

messages = ["It is certain",
    "It is decidedly so",
    "Yes definitely",
    "Reply hazy try again",
    "Ask again later",
    "Concentrate and ask again",
    "My reply is no",
    "Outlook not so good",
    "Very doubtful"]

print(messages[random.randint(0, len(messages) - 1)])
"""

# Conway"s Game of Life
"""
import random, time, copy
WIDTH = 60
HEIGHT = 20

# Create a list of list for the cells:
nextCells = []
for x in range(WIDTH):
    column = [] # Create a new column.
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append("#") # Add a living cell.
        else:
            column.append(" ") # Add a dead cell.
    nextCells.append(column) # nextCells is a list of column lists.

while True: # Main program loop.
    print("\n\n\n\n\n") # Separate each step with newlines.
    currentCells = copy.deepcopy(nextCells)

    # Print currentCells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end="") # Print the # or space.
        print() # Print a newline at the end of the row.

    # Calculate the next step"s cells based on current step"s cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighboring coordinates:
            # `% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
            leftCoord  = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Count number of living neighbors:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == "#":
                numNeighbors += 1 # Top-left neighbor is alive.
            if currentCells[x][aboveCoord] == "#":
                numNeighbors += 1 # Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == "#":
                numNeighbors += 1 # Top-right neighbor is alive.
            if currentCells[leftCoord][y] == "#":
                numNeighbors += 1 # Left neighbor is alive.
            if currentCells[rightCoord][y] == "#":
                numNeighbors += 1 # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == "#":
                numNeighbors += 1 # Bottom-left neighbor is alive.
            if currentCells[x][belowCoord] == "#":
                numNeighbors += 1 # Bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord] == "#":
                numNeighbors += 1 # Bottom-right neighbor is alive.

            # Set cell based on Conway"s Game of Life rules:
            if currentCells[x][y] == "#" and (numNeighbors == 2 or
numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                nextCells[x][y] = "#"
            elif currentCells[x][y] == " " and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                nextCells[x][y] = "#"
            else:
                # Everything else dies or stays dead:
                nextCells[x][y] = " "
    time.sleep(1) # Add a 1-second pause to reduce flickering.
"""

# Comma Code
"""
def comma_code(items):

    new_list = str

    if len(items) > 1:
        cut_list = items[0:-1]
        new_list = ", ".join(cut_list) + " and " + str(items[-1])
        return new_list
    elif len(items) == 1:
        return str(items[0])
    else:
        return "You gave me an empty list."

items = ["test", "test2", "test3"]
modified_list = comma_code(items)
print(modified_list)
"""

# Coin Flip Streaks
"""
import random
numberOfStreaks = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 "heads" or "tails" values.
    heads_or_tails = []
    for i in range(100):
        flip = random.randint(0, 1)
        if flip == 0:
            heads_or_tails.append("H")
        elif flip == 1:
            heads_or_tails.append("T")
    # Code that checks if there is a streak of 6 heads or tails in a row.
    previous_value = ""
    consecutive_values = 1

    for i in (heads_or_tails):
        if i == previous_value:
            consecutive_values += 1
        else:
            consecutive_values = 1
            previous_value = i
        if consecutive_values >= 6:
            numberOfStreaks += 1
            break

print("Chance of streak: %s%%" % (numberOfStreaks / 100))
"""

# Character Picture Grid

grid = [[".", ".", ".", ".", ".", "."],
        [".", "O", "O", ".", ".", "."],
        ["O", "O", "O", "O", ".", "."],
        ["O", "O", "O", "O", "O", "."],
        [".", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "."],
        ["O", "O", "O", "O", ".", "."],
        [".", "O", "O", ".", ".", "."],
        [".", ".", ".", ".", ".", "."]]

for x in range(6):
    for y in range(9):
        print(str(grid[y][x]), end = "")
    print()