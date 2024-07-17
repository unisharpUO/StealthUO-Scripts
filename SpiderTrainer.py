from helpers import *


Confidence = False
Meditating = False
Spider = 0x00468344


def OnClilocSpeech(_param1, _param2, _param3, _message):
    global Confidence, Meditating
    if 'exude' in _message:
        Confidence = True
    elif 'wanes' in _message:
        Confidence = False
    elif 'meditative' in _message:
        Meditating = True
    elif 'concentration' in _message:
        Meditating = False


def Meditate():
    global Meditating
    while GetMana(Self()) < GetMaxMana(Self()):
        while GetX(Self()) != 1062 or GetY(Self()) != 1362:
            print('moving1')
            MoveXY(1062, 1362, True, 0, True)
            Wait(100)
        if not Meditating:
            UseSkill('Meditation')
        Wait(1000)
    Equip(RhandLayer(), 0x4622F0A6)
    Meditating = False
    while GetX(Self()) != 1061 or GetY(Self()) != 1362:
        print('moving2')
        MoveXY(1061, 1362, True, 0, True)
        Wait(100)


if __name__ == '__main__':
    SetEventProc('evclilocspeech', OnClilocSpeech)

    Equip(RhandLayer(), 0x4622F0A6)

    print('attacking spider')
    Attack(Spider)

    while True:

        print('checking connection')
        if not Connected():
            Connect()
            Wait(10000)

        print('checking mana')
        if GetMana(Self()) < 6:
            Meditate()

        print('checking health')
        if GetHP(Self()) < GetMaxHP(Self()):
            while GetX(Self()) != 1062 or GetY(Self()) != 1362:
                print('moving1')
                MoveXY(1062, 1362, True, 0, True)
                Wait(100)
            if not Confidence:
                AddToSystemJournal("using confidence")
                Cast("Confidence")
                Wait(1250)
        else:
            while GetX(Self()) != 1061 or GetY(Self()) != 1362:
                print('moving2')
                MoveXY(1061, 1362, True, 0, True)
                Wait(100)

        print('checking ability')
        _ability = IsActiveSpellAbility("Momentum Strike")
        if not _ability:
            Cast('Momentum Strike')

        print('looping')
        Wait(1300)
