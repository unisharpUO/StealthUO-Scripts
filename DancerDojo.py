from py_stealth import *
from helpers import *
from datetime import datetime


Confidence = False
FanDancer = 0x0F7
Corpse = 0x2006
LootBag = 0
SendingBag = 0
PlayerTypes = [183, 184, 185, 186, 400, 401, 402, 403, 605, 606, 607, 608, 666,
               667, 694, 695, 750, 751, 970]


# entrance 79, 97, 326, 344 - bloodyroom 104, 115, 640, 660
def OnDrawObject(_objID):
    if _objID != Self():
        if GetType(_objID) in PlayerTypes:
            _tooltipRec = GetTooltipRec(_objID)
            if len(_tooltipRec) > 0:
                if _tooltipRec[0]['Cliloc_ID'] == 1050045:
                    _name = _tooltipRec[0]['Params'][1]
                    _now = datetime.now()
                    _now = _now.strftime("%m/%d/%Y %H:%M:%S")
                    AddToSystemJournal(f'Player Found: {_name} at {_now}')
    return


def OnClilocSpeech(_param1, _param2, _param3, _message):
    global Confidence
    if 'exude' in _message:
        Confidence = True
    elif 'wanes' in _message:
        Confidence = False
    return


def CheckWeight():
    if (Weight() >= MaxWeight()) and (SendingBag != 0):
        if FindTypeEx(0x0EED, 0xFFFF, Backpack(), True):
            _gold = GetFoundList()
            UseObject(SendingBag)
            Wait(1500)
            WaitTargetObject(_gold[0])
        else:
            AddToSystemJournal("I'm overweight and I can't find gold to send..")


def LootCorpse(_corpse):
    UseObject(_corpse)
    Wait(1500)
    if FindTypesArrayEx([0xFFFF], [0xFFFF], [_corpse], True):
        _lootList = GetFindedList()
        for _loot in _lootList:
            if (GetType(_loot) == 0x0EED) and (SendingBag != 0):
                _count = GetQuantity(_loot)
                MoveItem(_loot, _count, LootBag, 0, 0, 0)
            _tooltipRec = GetTooltipRec(_loot)
            if GetParam(_tooltipRec, 1112857) >= 20 and not\
                    ClilocIDExists(_tooltipRec, 1152714) and not\
                    ClilocIDExists(_tooltipRec, 1049643):
                AddToSystemJournal(f'Looting Item: {_loot}')
                MoveItem(_loot, 1, LootBag, 0, 0, 0)
                InsureItem(_loot)
    Ignore(_corpse)
    return


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
        else:
            _i += 1
            AddToSystemJournal("Couldn't find insure menu item.")
    CancelAllMenuHooks()
    CancelTarget()
    return


if __name__ == '__main__':
    SetEventProc('evclilocspeech', OnClilocSpeech)
    SetEventProc('evdrawobject', OnDrawObject)
    SetFindDistance(20)
    SetFindVertical(20)
    SetDropDelay(850)
    UseObject(Backpack())
    Wait(850)
    if FindTypesArrayEx([0x0E76], [0xFFFF], [Backpack()], True):
        _bags = GetFindedList()
        for _bag in _bags:
            # make sure they are bags of sending
            if 'sending' in GetTooltip(_bag).split('|')[0]:
                AddToSystemJournal("Found bag of sending...")
                SendingBag = _bag
    Wait(850)
    if FindTypesArrayEx([0xFFFF], [0xFFFF], [Backpack()], True):
        _ignoreList = GetFindedList()
        for _ignoreItem in _ignoreList:
            Ignore(_ignoreItem)
    AddToSystemJournal('Target your loot bag...')
    LootBag = RequestTarget()
    UseObject(LootBag)
    _monsters = []
    _corpses = []
    _lootedCorpses = []
    _currentTarget = 0

    while True:
        ClearBadLocationList()

        while not Connected():
            Connect()
            Wait(10000)

        CheckWeight()

        if FindTypesArrayEx([FanDancer], [0xFFFF], [0x0], True):
            _monsters = GetFindedList()

        # entrance 79, 97, 326, 344 - bloodyroom 104, 115, 640, 660
        if (_currentTarget == 0 and len(_monsters) > 0) or\
                (len(_monsters) > 0 and _currentTarget != 0 and
                 not IsObjectExists(_currentTarget)):
            if 79 <= GetX(_monsters[0]) <= 97 and\
                    326 <= GetY(_monsters[0]) <= 344:
                _currentTarget = _monsters[0]
                AddToSystemJournal(f'Current Target: {_currentTarget}')
                ReqVirtuesGump()
                UseVirtue('honor')
                WaitTargetObject(_currentTarget)
                Attack(_currentTarget)

        if _currentTarget != 0 and IsObjectExists(_currentTarget):
            NewMoveXY(GetX(_currentTarget), GetY(_currentTarget), False, 1,
                      True)
            Attack(_currentTarget)

        if GetHP(Self()) <= 90 and not Confidence:
            Cast('Confidence')

        if GetMana(Self()) >= 40:
            UsePrimaryAbility()

        if FindTypesArrayEx([Corpse], [0xFFFF], [0x0], True):
            _corpses = GetFindedList()

        if len(_corpses) > 0:
            for _corpse in _corpses:

                if _corpse in _lootedCorpses:
                    continue

                if GetDistance(_corpse) < 3:
                    LootCorpse(_corpse)
                    Ignore(_corpse)
                    _lootedCorpses.append(_corpse)
                else:
                    if 79 <= GetX(_corpse) <= 97 and\
                            326 <= GetY(_corpse) <= 344:
                        NewMoveXY(GetX(_corpse), GetY(_corpse), True, 0, True)
                        LootCorpse(_corpse)
                        Ignore(_corpse)
                        _lootedCorpses.append(_corpse)
        Wait(1000)
