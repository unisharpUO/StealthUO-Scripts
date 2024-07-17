import sys
from lib.helpers import *
from lib.armor import *
from lib.items import *
from lib.jewelry import *
import json
import tkinter as tk


ArmorList = []
JewelList = []


def SearchContainer():
    _container = RequestTarget()
    # _container = 0x42FC0327
    UseObject(_container)
    Wait(250)
    if FindTypesArrayEx([0xFFFF], [0xFFFF], [_container], True):
        _items = GetFindedList()
        for _item in _items:
            if GetType(_item) in JewelTypes:
                JewelList.append(Jewelry(_item))
    _message = f'Container searched, {len(JewelList)} items found.'
    print(_message)


def WriteToFile():
    FilePath = "export.json"
    _file = open(FilePath, 'w')
    _file.write("[")
    _i = 0
    for _item in JewelList:
        _file.write(json.dumps((_item.Encoder())))
        if _i != (len(JewelList) - 1):
            _file.write(',')
            _file.write('\n')
        _i += 1
    _file.write("]")
    _message = f'Exported {len(JewelList)} items.'
    _file.close()
    print(_message)


if __name__ == '__main__':
    window = tk.Tk()
    greeting = tk.Label(text="Hello, Tkinter")
    greeting.pack()
    window.mainloop()
    print('test')