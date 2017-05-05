#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from entity import *

oFirstCharacter = entityCharacter.Character(5, "First")
oSecondCharacter = entityMonster.Monster(10, "Second")

bContinue = True

while(bContinue):
    oFirstCharacter.attack(oSecondCharacter)
    if (oSecondCharacter.dComponent['ComponentLife'].iLife > 0):
        oSecondCharacter.attack(oFirstCharacter)
    else:
        print('{sName} winned' . format(sName = oFirstCharacter.sName))
        bContinue = False
        break;

    if (oFirstCharacter.dComponent['ComponentLife'].iLife < 0):
        print('{sName} winned' . format(sName = oSecondCharacter.sName))
        bContinue = False
        break;
