from py_stealth import *
import time


class runebook:
    def __init__(self, _runebookName, _method, _offsetName):
        self._runebookName = _runebookName
        self._method = _method
        self._runebook = ""
        self._failedRecall = False
        SetEventProc("evClilocSpeech", self.onClilocSpeech)
        if _offsetName == "osi":
            self._offset = 49
        else:
            self._offset = 0
        if FindType(0x22C5, Backpack()):
            _findList = GetFindedList()
            for _runebook in _findList:
                if (GetTooltip(_runebook).rsplit('|', 1)[1]) in\
                        self._runebookName:
                    self._runebook = _runebook
            if self._runebook == "":
                AddToSystemJournal("Runebook not found")
        else:
            AddToSystemJournal("Runebook not found")

    @property
    def Runebook(self):
        return self._runebook

    @property
    def RunebookName(self):
        return self._runebookName

    @property
    def Method(self):
        return self._method

    @property
    def Offset(self):
        return self._offset

    def Recall(self, _rune):
        if self.Runebook == "":
            AddToSystemJournal("Runebook not found")
            return
        self._failedRecall = False
        while Mana() < 25:
            UseSkill("Meditation")
            Wait(5000)
        UseObject(self.Runebook)
        Wait(500)
        if IsGump():
            for _gumpID in range(0, (GetGumpsCount())):
                _gump = GetGumpInfo(_gumpID)
                if 'GumpID' in _gump:
                    if _gump['Serial'] == self.Runebook:
                        NumGumpButton(_gumpID, _rune + self._offset)
            Wait(2500)
            if self._failedRecall:
                return False
            else:
                Wait(2000)
                return True
        else:
            AddToSystemJournal("Couldnt find gump")
            return False

    def onClilocSpeech(self, _arg1, _arg2, _arg3, _arg4):
        if "blocking" in _arg4:
            self._failedRecall = True
