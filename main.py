#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

import Character

oFirstCharacter = Character.Character("First")
oSecondCharacter = Character.Character("Second")

bContinue = True

while(bContinue):
    oFirstCharacter.attack(oSecondCharacter)
    if (oSecondCharacter.iLife > 0):
        oSecondCharacter.attack(oFirstCharacter)
    else:
        print('{sName} winned' . format(sName = oFirstCharacter.sName))
        bContinue = False
        break;

    if (oFirstCharacter.iLife < 0):
        print('{sName} winned' . format(sName = oSecondCharacter.sName))
        bContinue = False
        break;
