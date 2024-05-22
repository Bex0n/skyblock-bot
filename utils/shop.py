import time

from utils.moving import rotateDegrees, moveForward, command, click
from shared import is_running

def teleportToBuy():
    if is_running():
        print("Teleporting to shop")
        command('/warp sklep')

def teleportToSell():
    if is_running():
        print("Teleporting to shop")
        command('/warp skup')

def estimateSellClicks():
    return 30

def sellItems(item: str = None):
    if is_running():
        if item == "sugar_cane":
            moveToSugarCane()
        elif item == "wool":
            moveToWool()
        else:
            raise ValueError("Invalid item to sell")

        clicks = estimateSellClicks()
        for _ in range(clicks):
            if not is_running():
                break
            click(1)
            time.sleep(0.32)

def moveToSugarCane():
    if is_running():
        moveForward(2)
        rotateDegrees(-90)
        moveForward(2)

def moveToWool():
    if is_running():
        moveForward(0.2)
        rotateDegrees(52)
        moveForward(2.6)
