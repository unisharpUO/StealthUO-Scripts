from helpers import *


def OnClilocSpeech(_param1, _param2, _param3, _message):
    if 'Hat' in _message:
        InsureHats()


def InsureHats():
    if FindTypesArrayEx([5915], [0xFFFF], [Backpack()], True):
        for hat in GetFindedList():
            if 'Insured' not in GetTooltip(hat):
                Wait(250)
                RequestContextMenu(Self())
                _i = 0
                for _menuItem in GetContextMenu():
                    if "Toggle Item Insurance" in _menuItem:
                        SetContextMenuHook(Self(), _i)
                        Wait(250)
                        WaitTargetObject(hat)
                        Wait(250)
                        CancelMenu()
                        print(f'insured item')
                    else:
                        _i += 1
                CancelAllMenuHooks()
                CancelTarget()
                ClearContextMenu()
                Wait(250)


if __name__ == '__main__':
    SetEventProc('evclilocspeech', OnClilocSpeech)
    SetFindDistance(12)
    SetFindVertical(12)
    VortexTimer = time.time()
    UseVortex = True

    while True:
        Wait(500)

        if IsDead(Self()) or not Connected():
            exit()

        if time.time() - VortexTimer > 59 and UseVortex:
            Cast('Energy Vortex')
            WaitForTarget(2500)
            TargetToTile(0x0, 5586, 2013, 0)
            VortexTimer = time.time()

        if GetHP(Self()) < GetMaxHP(Self()):
            UseSkill('Peacemaking')
            WaitTargetSelf()
            Wait(250)
            CastToObj('Heal', Self())
            Wait(500)

        if FindTypesArrayEx(PlayerTypes, [0xFFFF], [0x0], True):
            for found in GetFindedList():
                Wait(150)
                if GetNotoriety(found) == 1 and not IsDead(found):
                    RequestStats(found)
                    if GetHP(found) < GetMaxHP(found) and not IsPoisoned(found):
                        CastToObj('Heal', found)
                        #print(f'Healing: {found} - {GetTooltip(found)} - {GetHP(found)}')
                        Wait(500)
                    if IsPoisoned(found):
                        CastToObj('Arch Cure', found)
                        Wait(1500)
