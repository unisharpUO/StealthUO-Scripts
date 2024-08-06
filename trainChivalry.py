from helpers import *


while True:
    Chivalry = GetSkillCurrentValue('Chivalry')

    if Chivalry >= 94:
        exit()

    if GetMana(Self()) < 10:
        while GetMana(Self()) < GetMaxMana(Self()):
            UseSkill('Meditation')
            Wait(2500)

    if GetHP(Self()) < 30:
        while GetHP(Self()) != GetMaxHP(Self()):
            Wait(1500)

    if Chivalry < 60:
        Cast('Divine Fury')
        Wait(500)
    elif 60 <= Chivalry < 70:
        Cast('Enemy of One')
        Wait(500)
    elif 70 <= Chivalry < 90:
        Cast('Holy Light')
        Wait(1000)
    elif 90 <= Chivalry < 100:
        Cast('Noble Sacrifice')
        Wait(1000)
