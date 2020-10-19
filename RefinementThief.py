from lib.helpers import *
from py_stealth import *
from lib.runebook import runebook
import datetime


# globals
RefinementBook = runebook("Refinements", "magery", "osi")
HomeBook = runebook("Home", "magery", "osi")
Storage = 1131454660
RefinementTypes = [0x4CD9, 0x142B, 0x2D61, 0x4CD8, 0x142A, 0x4CDA]
SetDropDelay(1500)
SetMoveThroughNPC(True)
Lockpicks = []
CriminalTimer = time.time()
Blocked = False
Picked = False
Minoc1 = [1, [2516, 561], 1073990757]
Minoc2 = [2, [2516, 561], 1073939601, 1073939624, 1074115148, 1074360321,
          1074214440, 1073992269, 1073992217, 1073992214, 1101738028]
Vesper1 = [3, [2923, 857], 1073998671]
Ocllo1 = [4, [], 1076462293]
Ocllo2 = [5, [], 1073956203]
Jhelom1 = [6, [], 1076228903]
Jhelom2 = [7, [], 1074025514]
Jhelom3 = [8, [], 1076227802]
Jhelom4 = [9, [], 1074026040]
Jhelom5 = [10, [], 1074026166]
Jhelom6 = [11, [], 1074026639]
Britain1 = [12, [], 1073931021]
Britain2 = [13, [], 1073930118]
Skara1 = [14, [637, 2219], 1074049091, 1076318930, 1074049095]
Serpents1 = [15, [], 1073977418, 1076463925, 1073977417, 1073977415, 1073977416,
             1076130026, 1076129830]


RefinementsSpots = [Skara1, Serpents1, Minoc1, Minoc2, Vesper1, Ocllo1, Ocllo2,
                    Jhelom1, Jhelom2, Jhelom3, Jhelom4, Jhelom5, Jhelom6,
                    Britain1, Britain2]


def OnClilocSpeech(_param1, _param2, _param3, _message):
    global Blocked, Picked, CriminalTimer
    if "steal the item" in _message:
        CriminalTimer = time.time()
    elif "blocking the location" in _message:
        Blocked = True
    elif "cannot teleport into that area" in _message:
        Blocked = True
    elif "yields to your skill" in _message:
        Picked = True


def CriminalTimerReset():
    global CriminalTimer, Criminal
    Criminal = True
    CriminalTimer = time.time()


def DumpRefinements():
    if FindTypesArrayEx(RefinementTypes, [0xFFFF], [Backpack()], False):
        _foundList = GetFindedList()
        print(f'refinements found, dumping')
        Wait(250)
        HomeBook.Recall(5)
        NewMoveXY(GetX(Storage), GetY(Storage), True, 1, True)
        Wait(500)
        UseObject(Storage)
        Wait(1500)
        for _found in _foundList:
            print(f'moving item: {_found}')
            MoveItem(_found, 1, Storage, 0, 0, 0)
        print(f'done dumping refinements')


def FindRefinements():
    global Blocked, Picked
    for _spot in RefinementsSpots:

        if IsDead(Self()):
            NewMoveXY(_spot[1][0], _spot[1][1], True, 1, True)

        UpdateLockpicks()
        RefinementBook.Recall(_spot[0])
        Wait(2000)

        if Blocked:
            Blocked = False
            continue

        for _box in _spot[2:]:

            while GetDistance(_box) > 1:
                NewMoveXY(GetX(_box), GetY(_box), True, 1, True)

            Wait(250)
            Picked = False
            while not Picked:
                UseObject(Lockpicks)
                Wait(250)
                TargetToObject(_box)
                Wait(1500)

            UseSkill("Remove Trap")
            Wait(250)
            TargetToObject(_box)
            Wait(10000)
            UseObject(_box)
            Wait(1500)

            if FindTypesArrayEx(RefinementTypes, [0xFFFF], [_box], False):
                _foundList = GetFindedList()
                UseSkill("Stealing")
                Wait(250)
                TargetToObject(_foundList[0])
                print(f'stole a refinement')
                Wait(15000)
            else:
                print(f'no refinements in box')

        _timeNow = time.time()
        _elapsed = CriminalTimer - now
        while _elapsed < 121:
            print(f'waiting for criminal status')
            UseSkill("Hiding")
            Wait(2000)


def UpdateLockpicks():
    print(f'checking lockpicks')
    global Lockpicks
    if FindType(0x14FB, Backpack()):
        Lockpicks = FindItem()
    else:
        MakeLockpicks()


def MakeLockpicks():
    print(f'making lockpicks')
    return


if __name__ == '__main__':
    while True:
        now = time.time()
        elapsed = now - CriminalTimer
        if elapsed > 120:
            print(f'two minutes have passed')
        Wait(1000)

    SetEventProc('evclilocspeech', OnClilocSpeech)
    AddToSystemJournal("starting RefinementThief")
    UseObject(Backpack())
    Wait(2000)

    while True:

        while not Connected():
            Connect()
            Wait(10000)

        UpdateLockpicks()

        DumpRefinements()

        FindRefinements()
