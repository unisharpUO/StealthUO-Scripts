from py_stealth import *
import time


def RequestTarget(_timeoutS=0):
    ClientRequestObjectTarget()
    _timeout = time.time() + _timeoutS
    while not ClientTargetResponsePresent():
        if _timeoutS != 0 and time.time() > _timeout:
            return ""
    return ClientTargetResponse()['ID']


def GetParam(_tooltipRec, _clilocID):
    for _tooltip in _tooltipRec:
        if _tooltip['Cliloc_ID'] == _clilocID:
            return int(_tooltip['Params'][0])
    return 0


def ClilocIDExists(_tooltipRec, _clilocID):
    for _tooltip in _tooltipRec:
        if _tooltip['Cliloc_ID'] == _clilocID:
            return True
    return False


def NewFind(_types, _colors, _container, _subs):
    _foundlist = []
    while True:
        try:
            Wait(250)
            if FindTypesArrayEx(_types, _colors, _container, _subs):
                _foundList = GetFindedList()
                _distanceList = []
                if len(_foundList) > 1:
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


def InsureItem(_item):
    Wait(250)
    RequestContextMenu(Self())
    _i = 0
    for _menuItem in GetContextMenu().splitlines():
        if "Toggle Item Insurance" in _menuItem:
            SetContextMenuHook(Self(), _i)
            Wait(250)
            WaitTargetObject(_item)
            Wait(250)
            CancelMenu()
            print(f'insured item')
        else:
            _i += 1
    CancelAllMenuHooks()
    CancelTarget()
    Wait(250)
    return
