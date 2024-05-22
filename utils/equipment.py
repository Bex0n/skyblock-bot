import time
from dotenv import load_dotenv
import os
import pynput
import pyautogui
from utils.moving import click

from shared import is_running

pyautogui.MINIMUM_DURATION = 0
pyautogui.MINIMUM_SLEEP = 0
pyautogui.PAUSE = 0

load_dotenv()

CHEST_ROWS = 6
CHEST_COLS = 9

CHEST_START = (
    int(os.getenv('CHEST_START_X', 1135)),
    int(os.getenv('CHEST_START_Y', 545))
)
CHEST_ITEM_INTERVAL = int(os.getenv('CHEST_ITEM_INTERVAL', 37))

def openChest():
    click(button=pynput.mouse.Button.right)

def closeChest():
    pyautogui.keyDown('e')
    time.sleep(0.1)
    pyautogui.keyUp('e')

def collectChest():
    for row in range(CHEST_ROWS):
        for col in range(CHEST_COLS):
            if not is_running():
                return
            pyautogui.keyDown('shift')
            pyautogui.moveTo(
                CHEST_START[0] + col * CHEST_ITEM_INTERVAL,
                CHEST_START[1] + row * CHEST_ITEM_INTERVAL,
            ),
            click()
            pyautogui.keyUp('shift')
            time.sleep(0.06)
