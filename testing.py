import json
from py_stealth import *
from helpers import *
from lib.weapon import *
from lib.jewelry import *


UseHeal = True
Bandaging = False


if __name__ == '__main__':
    _target = RequestTarget()
    UseObject(_target)
    Wait(250)
    _startTime = time.time()
    _foundList = []
    _weapons = []
    _jewelry = []
    if FindTypesArrayEx([0xFFFF], [0xFFFF], [_target], True):
        _foundList = GetFindedList()
        for _found in _foundList:
            _jewelry.append(Jewelry(_found))
    _endTime = time.time()
    print(f'{len(_jewelry)} weapons parsed in {_endTime - _startTime}')
    for _jewel in _jewelry:
        print(f'{json.dumps(_jewel.Encoder())}, ')
