from lib.helpers import *



def onPartyInvite(senderID):
    PartyAcceptInvite()
    Wait(500)


if __name__ == '__main__':
    SetEventProc('evPartyInvite', onPartyInvite)
    while True:
        if GetSkillCurrentValue('Chivalry') == 75:
            SetSkillLockState('Chivalry', 2)
            exit()

        Necro = GetSkillCurrentValue('Necromancy')

        if GetMana(Self()) < 10:
            while GetMana(Self()) < GetMaxMana(Self()):
                Wait(2500)

        Cast('Lich Form')
        Wait(1750)
