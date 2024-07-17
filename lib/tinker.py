from lib.helpers import *


class Tinker:
    def __init__(self, _id):
        if FindType(0x1EB9, Backpack()):
            _foundList = FindItem()
