from py_stealth import *
from datetime import datetime
import json
from json import JSONEncoder
import math
from pathlib import Path


class Jewelry:

    def __init__(self, _id):
        super().__init__()
        self.ID = _id
        self.Tooltip = GetTooltip(_id)
        self.TooltipRec = GetTooltipRec(_id)
        self.ItemName = self.Tooltip.split('|')[0]
        self.Antique = self.ClilocIDExists(1152714)
        self.Cursed = self.ClilocIDExists(1049643)
        self.Skills = self.CalcSkills()
        self.EnhancePotions = self.GetParam(1060411)
        self.DamageIncrease = self.GetParam(1060402)
        self.SwingSpeedIncrease = self.GetParam(1060486)
        self.FasterCasting = self.GetParam(1060413)
        self.FasterCastingRecovery = self.GetParam(1060412)
        self.SpellDamageIncrease = self.GetParam(1060483)
        self.ReflectPhysicalDamage = self.GetParam(1060442)
        self.DefenseChanceIncrease = self.GetParam(1060408)
        self.HitChanceIncrease = self.GetParam(1060415)
        self.Strength = self.GetParam(1060485)
        self.Dexterity = self.GetParam(1060409)
        self.Intelligence = self.GetParam(1060432)
        self.HitPointBonus = self.GetParam(1060431)
        self.StaminaBonus = self.GetParam(1060484)
        self.ManaBonus = self.GetParam(1060439)
        self.HitPointRegen = self.GetParam(1060444)
        self.StaminaRegen = self.GetParam(1060443)
        self.ManaRegen = self.GetParam(1060440)
        self.Luck = self.GetParam(1060436)
        # self.SkillType = GetParam(self.ToolTipRec, 1112857)

    def GetParam(self, _clilocID):
        for _tooltip in self.TooltipRec:
            if _tooltip['Cliloc_ID'] == _clilocID:
                return int(_tooltip['Params'][0])
        return 0

    def ClilocIDExists(self, _clilocID):
        for _tooltip in self.TooltipRec:
            if _tooltip['Cliloc_ID'] == _clilocID:
                return True
        return False

    def CalcSkills(self):
        # find out how many skills
        _numSkills = 0
        _skills = ""
        _clilocID = 1060451
        _weight = 1
        for _rec in self.Tooltip.split('|'):
            if "Weight" in _rec:
                break
            _weight += 1
        for _i in range(5):
            for _rec in self.TooltipRec:
                if _rec['Cliloc_ID'] == _clilocID + _i:
                    _numSkills += 1
                    # _skills += f"{_rec['Params'][0]}: {_rec['Params'][1]}, "
        for _s in range(_numSkills):
            _skills += f"{self.Tooltip.split('|')[_weight + _s]}, "
        return _skills.strip(", ")

    def Encoder(self):
        return {
            "ID": str(self.ID),
            "Name": str(self.ItemName),
            "Antique": str(self.Antique),
            "Cursed": str(self.Cursed),
            "EnhancePotions": str(self.EnhancePotions),
            "Skills": str(self.Skills),
            "DefenseChanceIncrease": str(self.DefenseChanceIncrease),
            "HitChanceIncrease": str(self.HitChanceIncrease),
            "DamageIncrease": str(self.DamageIncrease),
            "SwingSpeedIncrease": str(self.SwingSpeedIncrease),
            "FasterCasting": str(self.FasterCasting),
            "FasterCastingRecovery": str(self.FasterCastingRecovery),
            "SpellDamageIncrease": str(self.SpellDamageIncrease),
            "ReflectPhysicalDamage": str(self.ReflectPhysicalDamage),
            "Strength": str(self.Strength),
            "Intelligence": str(self.Intelligence),
            "HitPointBonus": str(self.HitPointBonus),
            "StaminaBonus": str(self.StaminaBonus),
            "ManaBonus": str(self.ManaBonus),
            "HitPointRegen": str(self.HitPointRegen),
            "StaminaRegen": str(self.StaminaRegen),
            "ManaRegen": str(self.ManaRegen),
            "Luck": str(self.Luck),
        }
