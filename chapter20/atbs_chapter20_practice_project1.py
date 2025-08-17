# Looking Busy

import pyautogui, time
wh = pyautogui.size()

try:
    while True:
        pyautogui.moveTo(wh[0]/2, wh[1]/2, duration=0.25)    # Click to make the window active.
        pyautogui.move(50, 50, duration=0.25)
        time.sleep(5)
except KeyboardInterrupt:
    print("Script cancelled.")