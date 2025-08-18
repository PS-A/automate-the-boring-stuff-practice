# 2048 - Play the game at https://gabrielecirulli.github.io/2048/

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://gabrielecirulli.github.io/2048/")

html_elem = driver.find_element(By.TAG_NAME, "html")

# Simple auto-move loop
moves = [Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT]

for i in range(5):
    for move in moves:
        html_elem.send_keys(move)
        time.sleep(0.1)
