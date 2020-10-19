from py_stealth import *
import time


def RequestTarget(_timeoutS=0):
    ClientRequestObjectTarget()
    _timeout = time.time() + _timeoutS
    while not ClientTargetResponsePresent():
        if _timeoutS != 0 and time.time() > _timeout:
            return ""
    return ClientTargetResponse()['ID']


def NewFind(_types, _colors, _container, _subs):
    _foundlist = []
    while True:
        try:
            Wait(250)
            if FindTypesArrayEx(_types, _colors, _container, _subs):
                _foundList = GetFindedList()
                _distanceList = []
                if len(_foundlist) > 1:
                    for _found in _foundList:
                        _distanceList.append(GetDistance(_found))
                    _orderedList = [_foundList[_i] for _i in _distanceList]
                    return _orderedList
                else:
                    return _foundList
            else:
                return []
        except Exception:
            AddToSystemJournal("Exception caught during find.")
            Wait(250)


if __name__ == '__main__':
    _watch = RequestTarget()
    _bandage = NewFind([0x0EE9, 0x0E21], [0xFFFF], [Backpack()], True)

    while True:
        if GetHP(_watch) < 90:
            UseObject(_bandage[0])
            WaitTargetObject(_watch)
            Wait(3000)
