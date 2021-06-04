from lib.helpers import *


if __name__ == '__main__':
    while True:

        if GetMana(Self()) < 10:
            while GetMana(Self()) < GetMaxMana(Self()):
                UseSkill('Meditation')
                Wait(1500)

        Cast('Resilience')
        Wait(750)
