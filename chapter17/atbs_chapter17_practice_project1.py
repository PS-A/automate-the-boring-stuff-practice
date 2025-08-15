# Prettified Stopwatch
#! python3

import time, pyperclip

# Display the program's instructions.
print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()                    # press Enter to begin
print('Started.')
startTime = time.time()    # get the first lap's start time
lastTime = startTime
lapNum = 1
text_output = []

# Start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        line = f'Lap #{str(lapNum).rjust(2)}: {str(totalTime).rjust(6)} ({str(lapTime).rjust(6)})'
        print(line)
        text_output.append(line)
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    pyperclip.copy("\n".join(text_output))
    print('\nDone.')