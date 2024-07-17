from helpers import *


def onPartyInvite(senderID):
    PartyAcceptInvite()
    Wait(500)


if __name__ == '__main__':
    SetEventProc('evPartyInvite', onPartyInvite)
    while True:
        if GetMana(Self()) < 10:
            while GetMana(Self()) < GetMaxMana(Self()):
                UseSkill('Meditation')
                Wait(2500)

        Cast('Curse Weapon')
        Wait(500)
