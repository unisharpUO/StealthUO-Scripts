from helpers import *

HatType = 5915
Container = 1178327643
if FindTypesArrayEx([HatType], [0xFFFF], [Backpack()], False):
    for hat in GetFindedList():
        MoveItem(hat, 1, Container, 0, 0, 0)
        Wait(1100)
