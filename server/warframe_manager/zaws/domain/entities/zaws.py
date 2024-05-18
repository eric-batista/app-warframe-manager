from enum import Enum

from devtools.models import Model


class OneHandedType(str, Enum):
    DAGGER = "DAGGER"
    MACHETE = "MACHETE"
    RAPIER = "RAPIER"
    SCYTHE = "SCYTHE"
    SWORD = "SWORD"
    NIKANA = "NIKANA"


class TwoHandedType(str, Enum):
    STAFF = "STAFF"
    POLEARM = "POLEARM"
    HEAVY_BLADE = "HEAVY_BLADE"
    HAMMER = "HAMMER"


class ZawStrike(Model):
    name: str
    img_url: str
    type_1h: OneHandedType
    type_2h: TwoHandedType
    base_damage: float
    speed: str
    critical_chance: str
    critical_multiplier: float
    status: str
    riven_disposition: float
    impact_damage: float
    puncture_damage: float | None
    slash_damage: float
    viral_damage: float | None

    def get_damage_value(self) -> float:
        return self.base_damage

    def get_critical_chance(self):
        return float(self.critical_chance.replace("%", ""))

    def get_attack_speed(self):
        speed_mult = self.speed
        if "+" in speed_mult:
            return float(speed_mult.removeprefix("+"))
        if "-" in speed_mult:
            return -float(speed_mult.removeprefix("-"))
        return 0.0

    def get_status_chance(self):
        return float(self.status.replace("%", ""))


class GripType(str, Enum):
    TWO_HANDED = "TWO_HANDED"
    ONE_HANDED = "ONE_HANDED"


class ZawGrip(Model):
    name: str
    img_url: str
    grip_type: GripType
    damage_bonus: str
    base_speed: float

    def _get_damage_factor_multiplier(self, strike_name: str) -> float:
        factor = {
            "Balla": 1.00,
            "Ooltha": 1.00,
            "Sepfahn": 1.00,
            "Plague Keewar": 0.85,
            "Cyath": 1.08,
            "Dehtat": 1.09,
            "Kronsh": 1.07,
            "Mewan": 1.09,
            "Plague Kripath": 1.08,
            "Rabvee": 1.08,
            "Dokrahm": 0.93,
            None: 1,
        }
        return factor[strike_name]

    def get_damage_factor(self, strike_name: str):
        damage_factor = {
            GripType.ONE_HANDED: 1,
            GripType.TWO_HANDED: self._get_damage_factor_multiplier(strike_name),
        }
        return damage_factor[self.grip_type]

    def get_damage_value(self) -> float:
        damage_calc = self.damage_bonus

        if "+" in damage_calc:
            return float(damage_calc.removeprefix("+"))
        if "-" in damage_calc:
            return -float(damage_calc.removeprefix("-"))
        return 0.0

    def get_attack_speed(self):
        return self.base_speed


class ZawLink(Model):
    name: str
    img_url: str
    speed_bonus: str
    critical_chance: str | None
    status_chance: str | None
    damage_bonus: str

    def get_damage_value(self) -> float:
        damage_calc = self.damage_bonus
        if "+" in damage_calc:
            return float(damage_calc.removeprefix("+"))
        if "-" in damage_calc:
            return -float(damage_calc.removeprefix("-"))
        return 0.0

    def get_critical_chance(self):
        if self.critical_chance:
            crit_chance = self.critical_chance.replace("%", "")
            if "+" in crit_chance:
                return float(crit_chance.removeprefix("+"))
            if "-" in crit_chance:
                return -float(crit_chance.removeprefix("-"))
            return 0.0

    def get_attack_speed(self):
        speed_mult = self.speed_bonus
        if "+" in speed_mult:
            return float(speed_mult.removeprefix("+"))
        if "-" in speed_mult:
            return -float(speed_mult.removeprefix("-"))
        return 0.0

    def get_status_chance(self):
        if self.status_chance:
            status_chance = self.status_chance.replace("%", "")
            if "+" in status_chance:
                return float(status_chance.removeprefix("+"))
            if "-" in status_chance:
                return -float(status_chance.removeprefix("-"))
            return 0.0


class Zaw(Model):
    strike: ZawStrike
    grip: ZawGrip
    link: ZawLink
    name: str
    level: str
    gild: bool

    def calculate_total_damage(self):
        return (
            self.strike.get_damage_value()
            + self.grip.get_damage_value()
            + self.link.get_damage_value()
        ) * self.grip.get_damage_factor(self.strike.name)

    def calculate_total_critical_chance(self):
        return self.strike.get_critical_chance() + self.link.get_critical_chance()

    def calculate_total_attack_speed(self):
        return (
            self.strike.get_attack_speed()
            + self.grip.get_attack_speed()
            + self.link.get_attack_speed()
        )

    def calculate_total_status_chance(self):
        return self.strike.get_status_chance() + self.link.get_status_chance()

    def get_parts_name(self):
        return f"{self.strike.name} + {self.grip.name} + {self.link.name}"
