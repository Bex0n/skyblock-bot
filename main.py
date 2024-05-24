import pyautogui
import time
from pynput import keyboard
import threading

import utils.shop as shop
import utils.moving as moving
import utils.ocr_reader as ocr_reader

from bots.sheeper import Sheeper
from bots.cactuser import Cactuser
from shared import running_event, stop_event, is_running

def on_press(key):
    if key == keyboard.Key.page_down:
        stop_event.set()
        return False
    if key == keyboard.Key.page_up:
        if running_event.is_set():
            running_event.clear()
            print("Bot stopped")
        else:
            running_event.set()
            print("Bot started")

def bot_actions():
    bot = Sheeper(sheep_stations=1)
    bot_2 = Cactuser(cactus_stations=1)
    try:
        while not stop_event.is_set():
            if is_running():
                # START OF BOT ACTIONS #

                bot.earn()
                time.sleep(10)
                bot_2.earn()
                time.sleep(50)

                # END OF BOT ACTIONS #
            time.sleep(1)
    except Exception as e:
        print(e)

def main():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    bot_thread = threading.Thread(target=bot_actions)
    bot_thread.start()

    listener.join()
    stop_event.set()
    bot_thread.join()

if __name__ == "__main__":
    main()
