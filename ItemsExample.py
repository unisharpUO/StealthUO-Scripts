import json
from py_stealth import *
from helpers import *
from lib.weapon import *
from lib.jewelry import *
from lib.armor import *


UseHeal = True
Bandaging = False


if __name__ == '__main__':
    while True:
        MoveItem(1124412412, 1, Backpack(), 0, 0, 0)
        Wait(5000000000)

    while True:
        _target = RequestTarget()
        UseObject(_target)
        Wait(1500)
        if FindTypesArrayEx([0xFFFF], [0xFFFF], [_target], False):
            _foundList = GetFindedList()
            for _found in _foundList:
                for _tip in GetTooltip(_found).split("|"):
                    if "Invulnerability" in _tip:
                        MoveItem(_found, 1, Backpack(), 0, 0, 0)
                        Wait(2000)

    # target container with armor
    _target = RequestTarget()
    UseObject(_target)
    Wait(250)

    if FindTypesArrayEx([0xFFFF], [0xFFFF], [_target], True):
        _foundList = GetFindedList()
        for _found in _foundList:
            # create new armor object with the found item
            _armor = Armor(_found)

            # if LMC is 10 and LRC is 25, move to backpack
            if _armor.LMC == 10 and _armor.LRC == 25:
                MoveItem(_armor.ID, 1, Backpack(), 0, 0, 0)

    # for _armor in _armors:
        # print(f'{json.dumps(_armor.Encoder())}, ')
