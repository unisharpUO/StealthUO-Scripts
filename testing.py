from py_stealth import *
from helpers import *
from lib.weapon import weapon


UseHeal = True
Bandaging = False


if __name__ == '__main__':
    _target = RequestTarget()
    _weapon = weapon(_target)
    print(f'damage type: {_weapon.ElementalDamage}')
