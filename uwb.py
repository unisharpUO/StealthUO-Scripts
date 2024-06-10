from lib.helpers import *


LeaderID = 37928828
AutoFollow = False


def onPartyInvite(senderID):
    if senderID == LeaderID:
        PartyAcceptInvite()
        Wait(500)


def onClilocSpeech(senderID, senderName, clilocID, message):
    print(message)


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
                print(f'AutoFollow: {AutoFollow}')


if __name__ == '__main__':
    SetFindVertical(20)
    SetFindDistance(20)
    SetEventProc('evPartyInvite', onPartyInvite)
    SetEventProc('evclilocspeech', onClilocSpeech)
    SetEventProc('evSpeech', onSpeech)
    SetMoveThroughCorner(0)
    SetMoveBetweenTwoCorners(0)
    SetMoveThroughNPC(0)

    while True:
        Wait(1000)

        if AutoFollow:
            if (GetX(Self()) != GetX(LeaderID)) or (GetY(Self()) != GetY(LeaderID)):
                MoveXY(GetX(LeaderID), GetY(LeaderID), False, 0, True)

        if GetHP(Self()) < 20:
            if GetActiveAbility() == "0":
                UsePrimaryAbility()
