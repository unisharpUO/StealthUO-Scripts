from helpers import *


SetFindDistance(20)
SetFindVertical(20)

animals = [207, 290, 208]

while True:
    found = []

    if FindTypesArrayEx(animals, [0xFFFF], [0x0], True):
        found = GetFoundList()

    for a in found:
        Attack(a)
        Wait(2000)

