from lib.helpers import *


LeaderID = 37928828
AutoFollow = False
Confidence = False


def onPartyInvite(senderID):
    if senderID == LeaderID:
        PartyAcceptInvite()
        Wait(500)


def onClilocSpeech(senderID, senderName, clilocID, message):
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
    SpiritSpeak = False
    Fencing = False
    Bushido = False
    Chivalry = False
    BossType = 704
    # Nosfentor |Shadowlord of Cowardice

    if GetSkillCurrentValue('Spirit Speak') > 90:
        SpiritSpeak = True

    if GetSkillCurrentValue('Fencing') > 90:
        Fencing = True

    if GetSkillCurrentValue('Bushido') > 90:
        Bushido = True

    if GetSkillCurrentValue('Chivalry') > 60:
        Chivalry = True

    while True:
        Wait(250)

        if AutoFollow:
            if (GetX(Self()) != GetX(LeaderID)) or (GetY(Self()) != GetY(LeaderID)):
                MoveXY(GetX(LeaderID), GetY(LeaderID), False, 0, True)

        if GetHP(Self()) < (GetMaxHP(Self()) - 20):
            if Bushido and not Confidence:
                Cast('Confidence')
                Wait(250)
            if GetActiveAbility() == "0" and Fencing:
                UsePrimaryAbility()
                Wait(250)
            if SpiritSpeak:
                UseSkill('Spirit Speak')
                Wait(250)
            if Chivalry:
                CastToObj('Close Wounds', Self())
                Wait(250)
            Wait(250)

        if not AutoFollow:
            if FindType(BossType, Ground()):
                ShadowLord = FindItem()
                if GetX(Self()) != GetX(ShadowLord) or GetY(Self()) != GetY(ShadowLord):
                    MoveXY(GetX(ShadowLord), GetY(ShadowLord), False, 0, True)
                Attack(ShadowLord)

        if not AutoFollow and GetActiveAbility() == "0":
            UseSecondaryAbility()
