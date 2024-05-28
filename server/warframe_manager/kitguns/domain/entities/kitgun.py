from enum import Enum

from devtools.models import Model


class GripType(str, Enum):
    PRIMARY = "PRIMARY"
    SECONDARY = "SECONDARY"


class KitgunType(GripType): ...


class DamageStatus(str, Enum):
    IMPACT = "IMPACT"
    HEAT = "HEAT"
    RADIATION = "RADIATION"
    SLASH = "SLASH"
    PUNCTURE = "PUNCTURE"
    TOXIN = "TOXIN"


class KitgunGrip(Model):
    name: str
    grip_type: GripType
    base_damage_bonus: str
    fire_rate: float
    weapon_range: int | None = None
    recoil_bonus: str
    charge_rate_bonus: str


class KitgunChamber(Model):
    name: str
    status: list[DamageStatus]
    weapon_type: KitgunType


class KitgunLoader(Model):
    name: str
    critical_chance: str
    critical_multiplier: str
    status_chance: str
    magazine: int


class Kitgun(Model):
    name: str
    grip: KitgunGrip
    chamber: KitgunChamber
    loader: KitgunLoader
    level: int
    gild: bool
