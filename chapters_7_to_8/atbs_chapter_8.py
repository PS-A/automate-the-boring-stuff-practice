# Project: How to keep an idiot busy for hours
"""
import pyinputplus as pyip

while True:
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(prompt)
    if response == 'no':
        break
print('Thank you. Have a nice day.')
"""

# Project: Multiplication Quiz

import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    # Pick two random numbers:
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = "#%s: %s x %s = " % (questionNumber, num1, num2)
    try:
        # Right answers are handled by allowRegexes.
        # Wrong answers are handled by blockRegexes, with a custom message.
        pyip.inputStr(
            prompt,
            allowRegexes=["^%s$" % (num1 * num2)],
            blockRegexes=[(".*", "Incorrect!")],
            timeout=8,
            limit=3,
        )
    except pyip.TimeoutException:
        print("Out of time!")
    except pyip.RetryLimitException:
        print("Out of tries!")
    else:
        # This block runs if no exceptions were raised in the try block.
        print("Correct!")
        correctAnswers += 1
    time.sleep(1)  # Brief pause to let user see the result.
print("Score: %s / %s" % (correctAnswers, numberOfQuestions))
