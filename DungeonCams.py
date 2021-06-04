from py_stealth import *
from discord_webhook import DiscordWebhook
import time
from datetime import datetime

class DungeonCams:
    IgnoreList = [65966797, 67138517, 67139921, 67143126, 67138367, 67133485]
    PlayerTypes = [183, 184, 185, 186, 400, 401, 402, 403, 605, 606, 607, 608,
                   666,
                   667, 694, 695, 750, 751, 970]
    Found = []

    def OnDrawObject(_objID):
        if _objID != Self() and GetNotoriety(_objID) != 7 and\
                _objID not in DungeonCams.Found and\
                _objID not in DungeonCams.IgnoreList:
            if GetType(_objID) in DungeonCams.PlayerTypes:
                _tooltipRec = GetTooltipRec(_objID)
                if len(_tooltipRec) > 0:
                    if _tooltipRec[0]['Cliloc_ID'] == 1050045:
                        _name = _tooltipRec[0]['Params'][1]
                        _location = ""
                        if GetX(Self()) == 5677 and GetY(Self()) == 1413:
                            _location = "Fire Dungeon Entrance"
                        elif GetX(Self()) == 1996 and GetY(Self()) == 88:
                            _location = "Ice Dungeon Entrance"
                        elif GetX(Self()) == 1180 and GetY(Self()) == 2645:
                            _location = "Destard Dungeon Entrance"
                        elif GetX(Self()) == 4729 and GetY(Self()) == 3815:
                            _location = "Hythloth Dungeon Entrance"
                        elif GetX(Self()) == 1967 and GetY(Self()) == 2060:
                            _location = "Marble Entrance"
                        elif GetX(Self()) == 1635 and GetY(Self()) == 3324:
                            _location = "Delucia Entrance"
                        _now = datetime.now()
                        _currentTime = _now.strftime("%H:%M:%S")
                        _message = '[%s] Found: %s:%s at %s' % (_currentTime, _name, _objID, _location)
                        _username = ShardName()
                        _webhook = DiscordWebhook(
                            url='https://discord.com/api/webhooks/830082253707018272/pPqAFC0fES0EgthRdYedVOECx2V_IYJs4FJdGM85bHtTbftRhhwoUGmJtY_GLMSbPI8I',
                            content=_message,
                            username=_username)
                        _webhook.execute()
                        DungeonCams.Found.append(_objID)
                        AddToSystemJournal(_message)
        return


if __name__ == "__main__":

    while not Connected():
        Connect()
        Wait(10000)

    SetEventProc('evDrawObject', DungeonCams.OnDrawObject)
    _start = time.time()
    while True:

        while not Connected():
            Connect()
            Wait(10000)

        if not Hidden():
            UseSkill("Hiding")
            Wait(5000)
        else:
            Wait(5000)

        if time.time() - _start > 300:
            _start = time.time()
            DungeonCams.Found.clear()
