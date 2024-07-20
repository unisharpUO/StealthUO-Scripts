from lib.helpers import *


LeaderID = 8439902
AutoFollow = False
Confidence = False
CurseWeapon = False


def onPartyInvite(senderID):
    if senderID == LeaderID:
        PartyAcceptInvite()
        Wait(500)


def onBuff(senderID, buffID, enabled):
    global CurseWeapon
    if senderID == Self() and buffID == 1088:
        CurseWeapon = enabled


def onClilocSpeech(senderID, senderName, clilocID, message):
    global Confidence
    if 'exude' in message:
        Confidence = True
    elif 'wanes' in message:
        Confidence = False
    return


def onSpeech(message, senderName, senderID):
    global AutoFollow, LeaderID
    if senderID == LeaderID:
        match message:
            case "PartyPrivateMsg: drop party":
                if InParty():
                    PartyLeave()
            case "PartyPrivateMsg: eoo":
                Cast('Enemy of One')
                Wait(1500)
            case "PartyPrivateMsg: follow toggle":
                AutoFollow = not AutoFollow
            case "PartyPrivateMsg: step":
                Step(4)
            case "PartyPrivateMsg: use rope ladder":
                if FindType(2214, Ground()):
                    found = FindItem()
                    MoveXY(GetX(found), GetY(found), True, 1, True)
                    UseObject(found)
            case "PartyPrivateMsg: use ladder":
                if FindType(2212, Ground()):
                    found = FindItem()
                    MoveXY(GetX(found), GetY(found), True, 1, True)
                    UseObject(found)


if __name__ == '__main__':
    SetFindVertical(20)
    SetFindDistance(20)
    SetEventProc('evPartyInvite', onPartyInvite)
    SetEventProc('evclilocspeech', onClilocSpeech)
    SetEventProc('evSpeech', onSpeech)
    SetEventProc('evBuffDebuffSystem', onBuff)
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

        if not CurseWeapon:
            Cast('Curse Weapon')
            Wait(1250)

        if AutoFollow:
            if (GetX(Self()) != GetX(LeaderID)) or (GetY(Self()) != GetY(LeaderID)):
                MoveXY(GetX(LeaderID), GetY(LeaderID), False, 0, True)

        healed = False
        if GetHP(Self()) < (GetMaxHP(Self()) - 20) and not IsPoisoned(Self()):
            if Bushido and not Confidence:
                Cast('Confidence')
                Wait(250)
                healed = True
            if GetActiveAbility() == "0" and Fencing and not healed:
                UsePrimaryAbility()
                Wait(250)
                healed = True
            if SpiritSpeak and not healed:
                UseSkill('Spirit Speak')
                Wait(250)
                healed = True
            if Chivalry and not healed:
                CastToObj('Close Wounds', Self())
                Wait(250)
                healed = True
            Wait(250)

        if IsPoisoned(Self()):
            CastToObj('Cleanse by Fire', Self())
            Wait(1500)

        if not AutoFollow:
            if FindType(BossType, Ground()):
                ShadowLord = FindItem()
                if GetX(Self()) != GetX(ShadowLord) or GetY(Self()) != GetY(ShadowLord):
                    MoveXY(GetX(ShadowLord), GetY(ShadowLord), False, 1, True)
                Attack(ShadowLord)

        if not AutoFollow and GetActiveAbility() == "0" and GetMana(Self()) > 30:
            UsePrimaryAbility()
            Wait(500)
