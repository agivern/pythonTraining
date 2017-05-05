#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

import random
from component import *

class Monster:
    """ Character main class """

    def __init__(self, iLife, sName = "Monster"):
        self.dComponent = dict();
        self.dComponent['ComponentLife'] = componentLife.ComponentLife(iLife);
        self.sName = sName

    def attack(self, target):
        target.dComponent['ComponentLife'].iLife -= random.randrange(6)
