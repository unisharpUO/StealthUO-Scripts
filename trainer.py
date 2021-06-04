from lib.helpers import *


if __name__ == '__main__':
    Equip(RhandLayer(), 0x4585AD5A)
    while True:

        if GetMana(Self()) < 10:
            while GetMana(Self()) < GetMaxMana(Self()):
                UseSkill('Meditation')
                Wait(1500)
            Equip(RhandLayer(), 0x4585AD5A)

        Cast('Counter Attack')
        Wait(750)
