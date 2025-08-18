# Use the Clipboard to Read a Text Field

import pyperclip, time
import pyautogui as pag
import pygetwindow as gw

pag.PAUSE = 0.1

wins = gw.getWindowsWithTitle("Testing GUI Automation - Notepad")
if not wins:
    raise SystemExit("No Notepad-window found.")

win = wins[0]
if win.isMinimized:
    win.restore()
win.activate()
time.sleep(0.3)

x = win.left + max(100, min(200, win.width // 2))
y = win.top + max(100, min(200, win.height // 2))
pag.click(x, y)
pag.hotkey("ctrl", "a")
pag.hotkey("ctrl", "c")
print(pyperclip.paste())
