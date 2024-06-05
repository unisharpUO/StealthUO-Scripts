from lib.helpers import *
from lib.jewelry import *


def OnClilocSpeech(_param1, _param2, _param3, _message):
    if "The instrument you are trying to play is no longer in your backpack!" in _message:
        FindInstrument()
    elif "What instrument shall you play the music on?" in _message:
        FindInstrument()


def FindInstrument():
    FindTypesArrayEx([3741], [0xFFFF], [Backpack()], True)
    instruments = GetFindedList()
    Wait(1500)
    UseObject(instruments[0])


SetEventProc('evclilocspeech', OnClilocSpeech)

while True:

    if GetMana(Self()) < 10:
        while GetMana(Self()) < GetMaxMana(Self()):
            UseSkill('Meditation')
            Wait(2500)

    Cast('Invigorate')
    Wait(1750)
