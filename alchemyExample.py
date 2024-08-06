from lib.alchemy import *


Bottles = 3854
BloodMoss = 3963
MandrakeRoot = 3974
Ginseng = 3973
Garlic = 3972
GraveDust = 3983


if __name__ == '__main__':
    Alchemy = GetSkillCurrentValue('Alchemy')

    while True:
        Wait(10)
        if IsGump():
            NumGumpButton(0, 1999)
        else:
            Wait(1500)
            UseType(3739, 0xFFFF)