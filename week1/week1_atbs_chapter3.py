# Defining first function, super basic.
"""
def hello(name):
    print("Howdy, " + name + "!")

hello("PeePa")
"""

# Magic 8 ball thingy.
"""
import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It is certain"
    elif answerNumber == 2:
        return "It is decidedly so"
    elif answerNumber == 3:
        return "Yes"
    elif answerNumber == 4:
        return "Reply hazy try again"
    elif answerNumber == 5:
        return "Ask again later"
    elif answerNumber == 6:
        return "Concentrate and ask again"
    elif answerNumber == 7:
        return "My reply is no"
    elif answerNumber == 8:
        return "Outlook not so good"
    elif answerNumber == 9:
        return "Very doubtful"

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
"""

# Call stack testing.
"""
def a():
    print("a() starts")
    b()
    d()
    print("a() returns")

def b():
    print("b() starts")
    c()
    print("b() returns")

def c():
    print("c() starts")
    print("c() returns")

def d():
    print("d() starts")
    print("d() returns")
a()
"""

# Local and Global variables testing.
"""
def spam():
    eggs = "spam local"
    print(eggs)    # prints "spam local"

def bacon():
    eggs = "bacon local"
    print(eggs)    # prints "bacon local"
    spam()
    print(eggs)    # prints "bacon local"

eggs = "global"
bacon()
print(eggs)        # prints "global"
"""

# More Local/Global variable testing.
"""
def spam():
    global eggs
    eggs = "spam" # this is the global

def bacon():
    eggs = "bacon" # this is a local

def ham():
    print(eggs) # this is the global

eggs = 42 # this is the global
spam()
print(eggs)
"""

# Exception handling basics.
"""
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("Error: Invalid argument.")

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
"""

# Zigzag program.

import time, sys
indent = 0 # How many spaces to indent.
indentIncreasing = True # Whether the indentation is increasing or not.

try:
    while True: # The main program loop.
        print(" " * indent, end="")
        print("********")
        time.sleep(0.1) # Pause for 1/10 of a second.

        if indentIncreasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
                # Change direction:
                indentIncreasing = False

        else:
            # Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()