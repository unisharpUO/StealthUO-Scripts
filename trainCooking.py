from lib.helpers import *


if __name__ == '__main__':
    skillet = 2431
    container = 1154204537
    fishType = 2426

    UseType(2431, 0xFFFF)
    Wait(1500)

    while True:
        FindType(fishType, container)
        fishStack = GetFindedList()[0]
        DragItem(fishStack, 1)
        Wait(250)
        DropItem(Backpack(), 0, 0, 0)
        Wait(250)

        if IsGump():
            NumGumpButton(0, 1999)
        else:
            Wait(1500)
            UseType(2431, 0xFFFF)

        Wait(1000)
