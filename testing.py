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
        UseObject(1105522184)
        Wait(1500)
        MoveItem(1124412412, 1, Backpack(), 0, 0, 0)
        Wait(50000000)



    _target = RequestTarget()
    UseObject(_target)
    Wait(250)
    _startTime = time.time()
    _foundList = []
    _weapons = []
    _armors = []
    if FindTypesArrayEx([0xFFFF], [0xFFFF], [_target], True):
        _foundList = GetFindedList()
        for _found in _foundList:
            _armors.append(Armor(_found))
    _endTime = time.time()
    print(f'{len(_armors)} weapons parsed in {_endTime - _startTime}')
    for _armor in _armors:
        print(f'{json.dumps(_armor.Encoder())}, ')
