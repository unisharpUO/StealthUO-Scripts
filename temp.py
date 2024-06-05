from helpers import *


SetFindDistance(20)

while True:
    ghosts = []

    if FindTypesArrayEx([26], [0xFFFF], [0x0], True):
        ghosts = GetFoundList()

    for ghost in ghosts:
        Attack(ghost)
        Wait(500)

    Wait(1500)
