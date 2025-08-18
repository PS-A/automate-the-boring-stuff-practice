# Dictionary Birthday test
"""
birthdays = {"Alice": "Apr 1", "Bob": "Dec 12", "Carol": "Mar 4"}

while True:
    print("Enter a name: (blank to quit)")
    name = input()
    if name == "":
        break
    if name in birthdays:
        print(birthdays[name] + " is the birthday of " + name)
    else:
        print("I do not have birthday information for " + name)
        print("What is their birthday?")
        bday = input()
        birthdays[name] = bday
        print("Birthday database updated.")
"""

# Character Count with Pretty Print
"""
import pprint
message = "It was a bright cold day in April, and the clocks were striking thirteen."
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint(count)
"""

# Tic-Tac-Toe Board
"""
theBoard = {"top-L": " ", "top-M": " ", "top-R": " ",
            "mid-L": " ", "mid-M":" ", "mid-R": " ",
            "low-L": " ", "low-M": " ", "low-R": " "}

def printBoard(board):
    print(board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"])
    print(board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"])
    print(board["low-L"] + "|" + board["low-M"] + "|" + board["low-R"])
turn = "X"
for i in range(9):
     printBoard(theBoard)
     print("Turn for " + turn + ". Move on which space?")
     move = input()
     theBoard[move] = turn
     if turn == "X":
         turn = "O"
     else:
         turn = "X"

printBoard(theBoard)
"""

# Picnic Dictionary with dictionaries and lists.
"""
allGuests = {"Alice": {"apples": 5, "pretzels": 12},
             "Bob": {"ham sandwiches": 3, "apples": 2},
             "Carol": {"cups": 3, "apple pies": 1}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
         numBrought = numBrought + v.get(item, 0)
    return numBrought

print("Number of things being brought:")
print(" - Apples         " + str(totalBrought(allGuests, "apples")))
print(" - Cups           " + str(totalBrought(allGuests, "cups")))
print(" - Cakes          " + str(totalBrought(allGuests, "cakes")))
print(" - Ham Sandwiches " + str(totalBrought(allGuests, "ham sandwiches")))
print(" - Apple Pies     " + str(totalBrought(allGuests, "apple pies")))
"""

# Chess Dictionary Validator
"""
chess_board = {"1a":"wpawn", "6c":"wqueen", "3g":"bknight", "4c":"bking", "6e":"wking"}

def is_valid_chess_board(board):
    valid_pieces = ["pawn", "knight", "bishop", "rook", "queen", "king"]
    wpieces = 0
    wpawns = 0
    bpieces = 0
    bpawns = 0
    kings = list(board.values())
    if kings.count("wking") != 1 or kings.count("bking") != 1:
        return False

    for k, v in board.items():
        if k[0] in "12345678" and k[1] in "abcdefgh" and v[0] in "wb" and v[1:] in valid_pieces:
            if v[0] == "w" and v[1:] == "pawn":
                wpieces += 1
                wpawns += 1
            elif v[0] == "w":
                wpieces += 1
            elif v[0] == "b" and v[1:] == "pawn":
                bpieces += 1
                bpawns += 1
            elif v[0] == "b":
                bpieces += 1
        else:
            return False
    
    if wpieces > 16 or bpieces > 16 or wpawns > 8 or bpawns > 8:
        return False
    else:
        return True

valid_board = is_valid_chess_board(chess_board)
print(valid_board)
"""

# Fantasy Game Inventory

inventory = {"gold coin": 43, "rope": 1}
dragon_loot = [
    "gold coin",
    "dagger",
    "gold coin",
    "gold coin",
    "ruby",
    "Sword of the Thousand Hippos",
    "Trinket of Eternal Chocolate",
]


def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory


def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + " " + k)
        item_total += v
    print("Total number of items: " + str(item_total))


inventory = add_to_inventory(inventory, dragon_loot)
display_inventory(inventory)
