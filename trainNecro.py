from helpers import *


while True:
    Necromancy = GetSkillCurrentValue('Necromancy')

    if GetMana(Self()) < 10:
        while GetMana(Self()) < GetMaxMana(Self()):
            UseSkill('Meditation')
            Wait(2500)

    if GetHP(Self()) < 30:
        while GetHP(Self()) != GetMaxHP(Self()):
            Wait(1500)

    if Necromancy < 50:
        CastToObj('Pain Spike', Self())
        Wait(750)
    elif 50 <= Necromancy < 70:
        Cast('Horrific Beast')
        Wait(1750)
    elif 70 <= Necromancy < 90:
        Cast('Wither')
        Wait(1000)
    elif 90 <= Necromancy < 100:
        Cast('Lich Form')
        Wait(1500)
