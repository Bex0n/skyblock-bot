import time

from utils.shop import sellItems, teleportToSell
from utils.moving import command, rotateDegrees
from utils.equipment import collectChest, openChest, closeChest

from shared import is_running

class Sheeper:
    def __init__(self, sheep_stations):
        self.sheep_stations = sheep_stations
        self.curr_station = 1

    def teleportToStation(self, station):
        if station == 1:
            print("Teleporting to station 1")
            command('/is warp owce1')
        elif station == 2:
            print("Teleporting to station 2")
            command('/is warp owce2')
        else:
            print("Invalid station number")

    def collectWoolFromChest(self):
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

    def colectWoolFromStation(self, station):
        if not is_running():
            return
        rotateDegrees(-35)
        self.collectWoolFromChest()
        if not is_running():
            return
        rotateDegrees(35)
        self.collectWoolFromChest()
        if not is_running():
            return
        rotateDegrees(25)
        self.collectWoolFromChest()

    def collectWool(self):
        self.teleportToStation(self.curr_station)
        self.colectWoolFromStation(self.curr_station)
        self.curr_station += 1
        if self.curr_station > self.sheep_stations:
            self.curr_station = 1

    def earn(self):
        self.collectWool()
        print("Selling wool")
        if not is_running():
            return
        teleportToSell()
        sellItems("wool")
