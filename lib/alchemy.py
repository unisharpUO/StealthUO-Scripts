from lib.helpers import *


class Alchemy:
    def __init__(self, container):
        self.Container = container
        Bottle = 0xF0E
        BloodMoss = 0xF7B
        SpiderSilk = 0xF8D
        BlackPearl = 0xF7A
        Garlic = 0xF84
        MandrakeRoot = 0xF86
        Nightshade = 0xF88
        SulfurousAsh = 0xF8C
        Ginseng = 0xF85

        FindTypesArrayEx()

        if FindType(0x1EB9, Backpack()):
            _foundList = FindItem()
