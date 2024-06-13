from helpers import *


Container = RequestTarget()
if FindTypesArrayEx([0xFFFF], [0xFFFF], [Container], False):
    Found = GetFindedList()
    for item in Found:
        print(GetTooltip(item))