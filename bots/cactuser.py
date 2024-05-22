import time

from utils.shop import sellItems, teleportToSell
from utils.moving import command, rotateDegrees
from utils.equipment import collectChest, openChest, closeChest

from shared import is_running

class Cactuser:
    def __init__(self, cactus_stations):
        self.cactus_stations = cactus_stations
        self.curr_station = 1

    def teleportToStation(self, station):
        if station == 1:
            print("Teleporting to station 1")
            command('/is warp kaktus')
        else:
            print("Invalid station number")

    def collectCactusFromChest(self):
        if not is_running():
            return
        time.sleep(0.5)
        openChest()
        if not is_running():
            return
        time.sleep(0.5)
        collectChest()
        time.sleep(0.5)
        if not is_running():
            return
        closeChest()
        time.sleep(0.5)

    def colectCactusFromStation(self, station):
        if not is_running():
            return
        rotateDegrees(-25)
        self.collectCactusFromChest()
        if not is_running():
            return
        rotateDegrees(25)
        self.collectCactusFromChest()
        if not is_running():
            return
        rotateDegrees(20)
        self.collectCactusFromChest()

    def collectCactus(self):
        self.teleportToStation(self.curr_station)
        self.colectCactusFromStation(self.curr_station)
        self.curr_station += 1
        if self.curr_station > self.cactus_stations:
            self.curr_station = 1

    def earn(self):
        self.collectCactus()
        print("Selling cactus")
        if not is_running():
            return
        teleportToSell()
        sellItems("cactus")
