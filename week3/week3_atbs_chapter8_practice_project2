# Write Your Own Multiplication Quiz
# Trying my hand at Multiplication Quiz without copying from previous practice.

import pyinputplus as pyip
import random, time

question_number = 0
max_questions = 10
correct_answers = 0

for questions in range(max_questions):
    first_number = random.randint(0,9)
    second_number = random.randint(0,9)
    correct_answer = first_number * second_number
    prompt = f"#{question_number}: Calculate {first_number} * {second_number}\n"
    try:
        pyip.inputStr(prompt, allowRegexes=[f'^{correct_answer}$'],
                                blockRegexes=[('.*', 'Incorrect!')],
                                timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print("Correct!")
        correct_answers += 1
    question_number += 1
    time.sleep(1)

print(f"You had {correct_answers}/{max_questions} questions correct.")