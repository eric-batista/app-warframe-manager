from warframe_manager.zaws.application import usecases
from warframe_manager.zaws.domain.entities import zaws


class TestZaws:
    def test_create_zaw_link(self, database_adapter):
        props = {
            "name": "Jai",
            "img_url": "",
            "speed_bonus": "+0.083",
            "critical_chance": None,
            "status_chance": None,
            "damage_bonus": "-4",
        }
        zaw_link = zaws.ZawLink.model_validate(props)
        response = usecases.RegisterZawLink(zaw_link, database_adapter).execute()
        assert response

    def test_create_assembled_zaw(self, database_adapter):
        props = {
            "name": "Jai",
            "img_url": "",
            "speed_bonus": "+0.083",
            "critical_chance": None,
            "status_chance": None,
            "damage_bonus": "-4",
        }
        zaw_link = zaws.ZawLink.model_validate(props)
        response = usecases.RegisterZawLink(zaw_link, database_adapter).execute()
        assert response is not None
        assert response.name == zaw_link.name

        props = {
            "name": "Jayap",
            "img_url": "",
            "grip_type": "TWO_HANDED",
            "damage_bonus": "0",
            "base_speed": 0.917,
        }
        zaw_grip = zaws.ZawGrip.model_validate(props)
        response = usecases.RegisterZawGrip(zaw_grip, database_adapter).execute()
        assert response is not None
        assert response.name == zaw_grip.name

        props = {
            "name": "Kronsh",
            "img_url": "",
            "type_1h": "MACHETE",
            "type_2h": "POLEARM",
            "base_damage": 234.0,
            "impact_damage": 163.8,
            "puncture_damage": None,
            "slash_damage": 70.2,
            "viral_damage": None,
            "speed": "-0.067",
            "critical_chance": "18%",
            "critical_multiplier": 2.0,
            "status": "18%",
            "riven_disposition": 1.3,
        }

        zaw_strike = zaws.ZawStrike.model_validate(props)
        response = usecases.RegisterZawStrike(zaw_strike, database_adapter).execute()
        assert response is not None
        assert response.name == zaw_strike.name

        props = {
            "name": "Zaw",
            "strike": zaw_strike.model_dump(),
            "grip": zaw_grip.model_dump(),
            "link": zaw_link.model_dump(),
            "level": "0",
            "gild": False,
        }

        zaw = zaws.Zaw.model_validate(props)

        response: zaws.Zaw = usecases.RegisterZaw(
            zaw, database_adapter=database_adapter
        ).execute()
        assert response is not None
        assert response.name == zaw.name
