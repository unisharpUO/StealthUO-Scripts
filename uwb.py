from lib.helpers import *


LeaderID = 37928828
AutoFollow = False
Confidence = False
BossType = [704]


def onPartyInvite(senderID):
    if senderID == LeaderID:
        PartyAcceptInvite()
        Wait(500)


def onClilocSpeech(senderID, senderName, clilocID, message):
    print(message)
    global Confidence
    if 'exude' in message:
        Confidence = True
    elif 'wanes' in message:
        Confidence = False
    return


def onSpeech(message, senderName, senderID):
    global AutoFollow
    if senderID == LeaderID:
        match message:
            case "PartyChatMsg: drop party":
                if InParty():
                    PartyLeave()
            case "PartyChatMsg: eoo":
                Cast('Enemy of One')
                Wait(1500)
            case "PartyChatMsg: follow toggle":
                AutoFollow = not AutoFollow


if __name__ == '__main__':
    SetFindVertical(20)
    SetFindDistance(20)
    SetEventProc('evPartyInvite', onPartyInvite)
    SetEventProc('evclilocspeech', onClilocSpeech)
    SetEventProc('evSpeech', onSpeech)
    SetMoveThroughCorner(1)
    SetMoveBetweenTwoCorners(1)
    SetMoveThroughNPC(1)

    while True:
        Wait(500)

        if AutoFollow:
            if (GetX(Self()) != GetX(LeaderID)) or (GetY(Self()) != GetY(LeaderID)):
                MoveXY(GetX(LeaderID), GetY(LeaderID), False, 0, True)

        if GetHP(Self()) < (GetMaxHP(Self()) - 20):
            if not Confidence:
                Cast('Confidence')
                Wait(250)
            if GetActiveAbility() == "0":
                UsePrimaryAbility()

        if FindType(146, Ground()):
            ShadowLord = FindItem()
            if not AutoFollow:
                if GetX(Self()) != GetX(ShadowLord) or GetY(Self()) != GetY(ShadowLord):
                    MoveXY(GetX(ShadowLord), GetY(ShadowLord), False, 0, True)
                Attack(ShadowLord)
        else:
            ShadowLord = 0

        if GetActiveAbility() == "0":
            UseSecondaryAbility()
