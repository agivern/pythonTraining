#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

import random

class Character:
    """ Character main class """
    def __init__(self, sName = "Smith"):
        self.iLife = 10
        self.sName = sName

    def attack(self, target):
        target.iLife -= random.randrange(6)
