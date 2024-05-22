import time
from dotenv import load_dotenv
import pynput
import pyautogui
import os

from pynput.mouse import Button

from shared import is_running

load_dotenv()

# Define a variable which maps the pixels in moveRel to the degrees to rotate
DRAG_DISTANCE_PER_DEGREE = int(os.getenv('DRAG_DISTANCE_PER_DEGREE', 12))

mouse = pynput.mouse.Controller()

def rotateDegrees(degrees):
    """
    Rotate the player by the specified number of degrees
    """
    if is_running():
        sign = 1 if degrees > 0 else -1
        degrees = abs(degrees)
        degrees  = int(degrees * 1.08)
        while degrees > 0:
            mouse.move(DRAG_DISTANCE_PER_DEGREE * sign, 0)
            time.sleep(0.01)
            degrees -= 1

def moveForward(seconds):
    """
    Move the player forward for the specified number of seconds
    """
    if is_running():
        pyautogui.keyDown('w')
        time.sleep(seconds)
        pyautogui.keyUp('w')

def click(num_clicks=1, time_between_clicks=0.16, button=Button.left):
    """
    Perform a left click
    """
    if is_running():
        for _ in range(num_clicks):
            mouse.click(button, 1)
            if num_clicks > 1:
                time.sleep(time_between_clicks)

def command(command: str):
    """
    Type a command in the chat and press enter
    """
    if is_running():
        pyautogui.write(command, interval=0.1)
        time.sleep(0.2)
        pyautogui.press('enter')
        time.sleep(0.3)
