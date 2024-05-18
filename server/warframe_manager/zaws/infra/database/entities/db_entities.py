from enum import Enum
from typing import List

import sqlalchemy as sa
from devtools.database import AbstractEntity
from sqlalchemy.orm import Mapped, mapped_column, relationship


class GripType(str, Enum):
    TWO_HANDED = "two-handed"
    ONE_HANDED = "one-handed"


class OneHandedType(str, Enum):
    DAGGER = "dagger"
    MACHETE = "machete"
    RAPIER = "rapier"
    SCYTHE = "scythe"
    SWORD = "sword"
    NIKANA = "nikana"


class TwoHandedType(str, Enum):
    STAFF = "staff"
    POLEARM = "polearm"
    HEAVY_BLADE = "heavy-blade"
    HAMMER = "hammer"


class ZawGrip(AbstractEntity):
    id: Mapped[sa.UUID] = mapped_column(
        "id", sa.UUID, unique=True, primary_key=True, nullable=False, index=True
    )
    img_url = sa.Column("img_url", sa.Text, index=True)
    name = sa.Column("name", sa.Text, index=True, unique=True)
    created_at = sa.Column("created_at", sa.DateTime, nullable=False, index=True)
    updated_at = sa.Column("updated_at", sa.DateTime, nullable=True, index=True)
    grip_type = sa.Column("grip_type", sa.Enum(GripType), index=True)
    damage_bonus = sa.Column("damage_bonus", sa.Text, index=True)
    base_speed = sa.Column("base_speed", sa.Float, index=True)
    zaws: Mapped[List["Zaw"]] = relationship(back_populates="grip")


class ZawLink(AbstractEntity):
    id: Mapped[sa.UUID] = mapped_column(
        "id", sa.UUID, unique=True, primary_key=True, nullable=False, index=True
    )
    img_url = sa.Column("img_url", sa.Text, index=True)
    name = sa.Column("name", sa.Text, index=True, unique=True)
    created_at = sa.Column("created_at", sa.DateTime, nullable=False, index=True)
    updated_at = sa.Column("updated_at", sa.DateTime, nullable=True, index=True)
    speed_bonus = sa.Column("speed_bonus", sa.Text, index=True)
    critical_chance = sa.Column("critical_chance", sa.Text, nullable=True, index=True)
    status_chance = sa.Column("status_chance", sa.Text, nullable=True, index=True)
    damage_bonus = sa.Column("damage_bonus", sa.Text, index=True)
    zaws: Mapped[List["Zaw"]] = relationship(back_populates="link")


class ZawStrike(AbstractEntity):
    id: Mapped[sa.UUID] = mapped_column(
        "id", sa.UUID, unique=True, primary_key=True, nullable=False, index=True
    )
    img_url = sa.Column("img_url", sa.Text, index=True)
    name = sa.Column("name", sa.Text, index=True, unique=True)
    created_at = sa.Column("created_at", sa.DateTime, nullable=False, index=True)
    updated_at = sa.Column("updated_at", sa.DateTime, nullable=True, index=True)
    type_1h = sa.Column("type_1h", sa.Enum(OneHandedType), index=True)
    type_2h = sa.Column("type_2h", sa.Enum(TwoHandedType), index=True)
    base_damage = sa.Column("base_damage", sa.Float, index=True)
    speed = sa.Column("speed", sa.Text, index=True)
    critical_chance = sa.Column("critical_chance", sa.Text, index=True)
    critical_multiplier = sa.Column("critical_multiplier", sa.Float, index=True)
    status = sa.Column("status", sa.Text, index=True)
    riven_disposition = sa.Column("riven_disposition", sa.Float, index=True)
    impact_damage = sa.Column("impact_damage", sa.Float, index=True)
    puncture_damage = sa.Column("puncture_damage", sa.Float, index=True, nullable=True)
    slash_damage = sa.Column("slash_damage", sa.Float, index=True)
    viral_damage = sa.Column("viral_damage", sa.Float, index=True, nullable=True)
    zaws: Mapped[List["Zaw"]] = relationship(back_populates="strike")


class Zaw(AbstractEntity):
    id = sa.Column(
        "id", sa.UUID, unique=True, primary_key=True, nullable=False, index=True
    )
    name = sa.Column("name", sa.Text, index=True, unique=True)
    created_at = sa.Column("created_at", sa.DateTime, nullable=False, index=True)
    updated_at = sa.Column("updated_at", sa.DateTime, nullable=True, index=True)
    level = sa.Column("level", sa.Text, index=True)
    gild = sa.Column("gild", sa.Boolean, index=True)
    link_id = sa.Column(sa.ForeignKey("zawlink.id"))
    grip_id = sa.Column(sa.ForeignKey("zawgrip.id"))
    strike_id = sa.Column(sa.ForeignKey("zawstrike.id"))
    link: Mapped[ZawLink] = relationship(back_populates="zaws")
    grip: Mapped[ZawGrip] = relationship(back_populates="zaws")
    strike: Mapped[ZawStrike] = relationship(back_populates="zaws")
