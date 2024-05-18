import uuid

import sqlalchemy as sa
from devtools.database import DatabaseAdapter
from devtools.utils import timezone

from warframe_manager.zaws.application.dtos import zaws as dto_models
from warframe_manager.zaws.domain.entities import zaws as domain_models
from warframe_manager.zaws.infra.database.entities import db_entities


class ZawRepositoryDB:
    def __init__(self, adapter: DatabaseAdapter) -> None:
        self._context = adapter.context()

    def get_link_by_field(self, value, field) -> dto_models.ZawLink:
        query = sa.text(
            f"""
            SELECT * FROM zawlink WHERE {field} = '{value}'
            """
        )
        with self._context as conn:
            result = conn.execute(query)
            if not (values := result.fetchall()):
                raise Exception("link not found")
            return dto_models.ZawLink.model_validate(values[0])

    def get_grip_by_field(self, value, field):
        query = sa.text(
            f"""
            SELECT * FROM zawgrip WHERE {field} = '{value}'
            """
        )
        with self._context as conn:
            result = conn.execute(query)
            conn.commit()
            if not (values := result.fetchall()):
                raise Exception("grip not found")
            return dto_models.ZawGrip.model_validate(values[0])

    def get_strike_by_field(self, value, field):
        query = sa.text(
            f"""
            SELECT * FROM zawstrike WHERE {field} = '{value}'
            """
        )
        with self._context as conn:
            result = conn.execute(query)
            conn.commit()
            if not (values := result.fetchall()):
                raise Exception("strike not found")
            return dto_models.ZawStrike.model_validate(values[0])

    def create_zaw(self, zaw: domain_models.Zaw) -> dto_models.Zaw:
        try:
            link = self.get_link_by_field(zaw.link_id, "id")
            grip = self.get_grip_by_field(zaw.grip_id, "id")
            strike = self.get_strike_by_field(zaw.strike_id, "id")
        except Exception as e:
            raise e

        values = {
            "id": uuid.uuid4(),
            "name": zaw.name,
            "created_at": timezone.now(),
            "updated_at": None,
            "level": zaw.level,
            "gild": zaw.gild,
            "link_id": link.id,
            "grip_id": grip.id,
            "strike_id": strike.id,
        }

        query = sa.insert(db_entities.Zaw).values(values)

        with self._context as conn:
            conn.execute(query)
            conn.commit()

        return dto_models.Zaw.model_validate(values)

    def create_grip(self, zaw_grip: domain_models.ZawGrip) -> dto_models.ZawGrip:
        models_values = zaw_grip.model_dump()
        models_values.pop("grip_type")
        values = {
            "id": uuid.uuid4(),
            "created_at": timezone.now(),
            "updated_at": None,
            "grip_type": zaw_grip.grip_type.value,
            **models_values,
        }

        query = sa.insert(db_entities.ZawGrip).values(values)
        with self._context as conn:
            conn.execute(query)
            conn.commit()

        return dto_models.ZawGrip.model_validate(values)

    def create_link(self, zaw_link: domain_models.ZawLink) -> dto_models.ZawLink:
        values = {
            "id": uuid.uuid4(),
            "created_at": timezone.now(),
            "updated_at": None,
            **zaw_link.model_dump(),
        }

        query = sa.insert(db_entities.ZawLink).values(values)

        with self._context as conn:
            conn.execute(query)
            conn.commit()

        return dto_models.ZawLink.model_validate(values)

    def create_strike(
        self, zaw_strike: domain_models.ZawStrike
    ) -> dto_models.ZawStrike:
        values = {
            "id": uuid.uuid4(),
            "created_at": timezone.now(),
            "updated_at": None,
            **zaw_strike.model_dump(),
        }

        query = sa.insert(db_entities.ZawStrike).values(values)

        with self._context as conn:
            conn.execute(query)
            conn.commit()

        return dto_models.ZawStrike.model_validate(values)
