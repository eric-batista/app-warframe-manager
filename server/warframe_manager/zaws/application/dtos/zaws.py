from datetime import datetime
from uuid import UUID
from devtools.models import Model
from warframe_manager.zaws.domain.entities import zaws


class ZawGrip(zaws.ZawGrip):
    id: UUID
    created_at: datetime
    updated_at: datetime | None
    grip_type: str


class ZawLink(zaws.ZawLink):
    id: UUID
    created_at: datetime
    updated_at: datetime | None


class ZawStrike(zaws.ZawStrike):
    id: UUID
    created_at: datetime
    updated_at: datetime | None
    type_1h: str
    type_2h: str


class Zaw(zaws.Zaw):
    id: UUID
    created_at: datetime
    updated_at: datetime | None
    strike_id: UUID
    link_id: UUID
    grip_id: UUID
    strike: ZawStrike | None = None
    grip: ZawGrip | None = None
    link: ZawLink | None = None


class ZawRequest(Model):
    strike_id: UUID
    link_id: UUID
    grip_id: UUID
    name: str
    level: str
    gild: bool