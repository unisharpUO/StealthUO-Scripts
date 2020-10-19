from py_stealth import *
from datetime import datetime
import json
import math
from pathlib import Path


class weapon:

    def __init__(self, _id):
        super().__init__()
        self.ID = _id
        self.Tooltip = GetTooltip(_id)
        self.TooltipRec = GetTooltipRec(_id)
        self.ItemName = self.Tooltip.split('|')[0]
        self.Splintering = self.GetParam(1112857)
        self.HitLowerAttack = self.GetParam(1060424)
        self.HitLowerDefense = self.GetParam(1060425)
        self.SpellChanneling = self.ClilocIDExists(1060482)
        self.Balanced = self.ClilocIDExists(1072792)
        self.UseBestWeaponSkill = self.ClilocIDExists(1060400)
        self.MageWeapon = self.GetParam(1060438)
        self.BloodDrinker = self.ClilocIDExists(1113591)
        self.Velocity = self.GetParam(1072793)
        self.BattleLust = self.ClilocIDExists(1113710)
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
        self.EnhancePotions = self.GetParam(1060411)
        self.Luck = self.GetParam(1060436)
        self.Brittle = self.ClilocIDExists(1116209)
        self.Antique = self.ClilocIDExists(1152714)
        self.Cursed = self.ClilocIDExists(1049643)
        self.WeaponType = GetType(_id)
        # self.SkillType = GetParam(self.ToolTipRec, 1112857)
        # self.HitSpell = GetParam(self.ToolTipRec, 1112857)
        # self.HitArea = GetParam(self.ToolTipRec, 1112857)

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

    @property
    def HitSpell(self):

        return ""

    @property
    def ElementalDamage(self):
        _elementalDamage = ""
        if self.ClilocIDExists(1060403):
            _elementalDamage += f"Physical Damage {self.GetParam(1060403)} "
        if self.ClilocIDExists(1060404):
            _elementalDamage += f"Fire Damage {self.GetParam(1060404)} "
        if self.ClilocIDExists(1060405):
            _elementalDamage += f"Cold  Damage {self.GetParam(1060405)} "
        if self.ClilocIDExists(1060406):
            _elementalDamage += f"Poison  Damage {self.GetParam(1060406)} "
        if self.ClilocIDExists(1060407):
            _elementalDamage += f"Energy  Damage {self.GetParam(1060407)} "
        return _elementalDamage
