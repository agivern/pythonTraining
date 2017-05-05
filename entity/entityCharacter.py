#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

import random
from component import *

class Character:
    """ Character main class """

    sName = "Smith";
    dComponent = dict();
    def __init__(self, iLife, sName = "Smith"):
        Character.dComponent['ComponentLife'] = componentLife.ComponentLife(iLife);
        Character.sName = sName

    def attack(self, target):
        target.dComponent['ComponentLife'].iLife -= random.randrange(6)
