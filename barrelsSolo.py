from py_stealth import *
from helpers import *

GotKey = False
UseChiv = False
UseHeal = False
UseBush = True
Confidence = False

# top right room key = 16651
# top right room treasure = 3700
#
# barrel = 4014
# safe = 10334
# door right = 1761, 1757
# door left =
#
# top right room start = 6434,1735
# top left = 6428,1735
# bottom right = 6434,1752
# bottom left = 6428,1752

Doors = [1761, 1757]

# room format is, entrance coords, good barrels, bad barrels
RoomTopRight = [[6434, 1735], [6437, 1729], [6445, 1737], [6440, 1732], [6442, 1734]]
RoomTopLeft = [[6428, 1735], [6437, 1729], [6437, 1729], [6420, 1732], [6422, 1734]]
RoomBottomRight = [[6434, 1752], [6437, 1749], [6445, 1757], [6440, 1752], [6442, 1754]]
RoomBottomLeft = [[6428, 1752], [6417, 1749], [6425, 1757], [6420, 1752], [6422, 1754]]
Rooms = [RoomTopRight, RoomTopLeft, RoomBottomRight, RoomBottomLeft]


def OnClilocSpeech(_param1, _param2, _param3, _message):
    global Confidence
    if 'exude' in _message:
        Confidence = True
    elif 'wanes' in _message:
        Confidence = False
    return


def GetKey(_key):
    global GotKey
    NewMoveXY(GetX(_key), GetY(_key), True, 1, True)
    Wait(1500)
    MoveItem(_key, 1, Backpack(), 0, 0, 0)
    Wait(1500)
    GotKey = True
    return


def GetSafe(_room):
    SetFindDistance(2)
    _centerBarrels = GetCenterBarrels(_room)
    NewMoveXY(_centerBarrels[0], _centerBarrels[1], False, 0, False)
    _barrels = FindBarrels()
    _barrelsCoords = []
    for _barrel in _barrels:
        while GetDistance(_barrel) > 1:
            _dir = CalcDir(GetX(Self()), GetY(Self()),
                           GetX(_barrel), GetY(_barrel))
            print(f'Stepping')
            Step(_dir)
            Wait(250)
        AttackBarrels(_barrel)
        _barrels = FindBarrels()
        break
    return


# solid barrels color 2500
# regular barrels color 0


def FindBarrels():
    #SetFindDistance(8)
    _barrels = []
    _barrelsSorted = []
    if FindTypesArrayEx([4014, 7861, 3703], [0xFFFF], [0x0], False):
        _barrels = GetFindedList()
        _barrels = list(dict.fromkeys(_barrels))
        if len(_barrels) > 1:
            for _b in _barrels:
                _barrelsSorted.append(GetDistance(_b))
            _orderedList = [x for _, x in sorted(zip(_barrelsSorted, _barrels))]
            return _orderedList
        else:
            return _barrels
    else:
        AddToSystemJournal('No barrels, exiting.')
        exit()


def Heal():
    while GetHP(Self()) < (GetMaxHP(Self()) - 20):
        while IsPoisoned(Self()):
            Cure()
        if UseBush and not Confidence:
            print('using confidence to heal')
            Cast('Confidence')
        Wait(250)


def Cure():
    while IsPoisoned(Self()):
        print(f'trying to cure')
        if UseChiv:
            CastToObj('Cleanse By Fire', Self())
            Wait(2000)
        else:
            AddToSystemJournal("No way to cure")
            break
        Wait(250)


def GetCenterBarrels(_room):
    _points = []
    for _x in range(_room[3][0], _room[4][0] + 1):
        for _y in range(_room[3][1], _room[4][1] + 1):
            _points.append([_x, _y])
    return _points


def AttackBarrels(_barrel):
    SetWarMode(True)
    Attack(_barrel)
    print(f'attacking barrel')
    while IsObjectExists(_barrel):
        if GetActiveAbility() == "0" and GetMana(Self()) > 30:
            UsePrimaryAbility()
            Wait(500)
        while FindType(0x005C, 0x0):
            print(f'attacking serpent')
            Attack(FindItem())
            Wait(1500)
        while FindType(0x013D, 0x0):
            print(f'attacking bat')
            Attack(FindItem())
            Wait(1500)
        while FindType(24, 0x0):
            print(f'attacking lich')
            Attack(FindItem())
            Wait(1500)
        while FindType(215, 0x0):
            print(f'attacking rat')
            Attack(FindItem())
            Wait(1500)
        if GetHP(Self()) < (GetMaxHP(Self()) - 20):
            SetWarMode(False)
            Heal()
            print(f'done healing')
            SetWarMode(True)
            Attack(_barrel)
        if IsPoisoned(Self()):
            SetWarMode(False)
            Cure()
            print(f'done curing')
            SetWarMode(True)
            Attack(_barrel)
        if FindType(0x410B, 0x0):
            GetKey(FindItem())
        print('cycling 2s wait in AttackBarrels function')
        Wait(500)
        Attack(_barrel)


if __name__ == '__main__':
    SetEventProc('evClilocSpeech', OnClilocSpeech)

    SetMoveOpenDoor(True)
    SetMoveThroughNPC(True)

    if GetSkillValue("Chivalry") > 50:
        UseChiv = True
    if GetSkillValue("Bushido") > 50:
        UseBush = True

    roomCurrent = []
    for room in Rooms:
        if GetX(Self()) == room[0][0] and GetY(Self()) == room[0][1]:
            roomCurrent = room

    while (GetX(Self()) != roomCurrent[0][0]) or \
            (GetY(Self()) != roomCurrent[0][1]):
        NewMoveXY(roomCurrent[0][0], roomCurrent[0][1], False, 0, False)
        Wait(250)
    SetFindDistance(2)
    if FindTypesArrayEx(Doors, [0xFFFF], [0x0], True):
        _foundList = GetFindedList()
        if len(_foundList) > 0:
            UseObject(_foundList[0])
    else:
        AddToSystemJournal('No door, exiting.')
        exit()

    print(f'Door opened, next routine...')
    # at this point we've moved to the door and opened it

    if roomCurrent[0][0] == 6434:
        Step(2)
        Wait(500)
        Step(2)
        Wait(500)
        Step(2)
    else:
        Step(6)
        Wait(500)
        Step(6)
        Wait(500)
        Step(6)

    while not GotKey:
        SetFindDistance(8)
        _barrels = FindBarrels()
        _barrelsCoords = []
        _centerBarrels = GetCenterBarrels(roomCurrent)
        for _barrel in _barrels:
            if [GetX(_barrel), GetY(_barrel)] in _centerBarrels:
                continue
            count = 0
            while GetDistance(_barrel) > 1:
                IgnoreReset()
                _dir = CalcDir(GetX(Self()), GetY(Self()),
                               GetX(_barrel), GetY(_barrel))
                print(f'Stepping {_dir}')
                Step(_dir)
                Wait(250)
                count += 1
                if count > 3 and GetDirection(Self()) == 3:
                    print(f'Stepping 3')
                    Step(4)
                    Step(4)
                    count = 0
                elif count > 3 and GetDirection(Self()) == 1:
                    print(f'Stepping 1')
                    Step(2)
                    Step(2)
                    count = 0
                elif count > 3 and GetDirection(Self()) == 7:
                    print(f'Stepping 7')
                    Step(0)
                    Step(0)
                    count = 0
                elif count > 3 and GetDirection(Self()) == 5:
                    print(f'Stepping 5')
                    Step(6)
                    Step(6)
                    count = 0
            AttackBarrels(_barrel)
            _barrels = FindBarrels()
            break

    if GotKey:
        print('GOT KEY')
        GotKey = False
