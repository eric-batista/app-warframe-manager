from warframe_manager.zaws.domain.entities import zaws


class TestZawStrikes:
    def test_create_zaw_strike_without_optional_fields(self):
        props = {
            "name": "Kronsh",
            "img_url": "",
            "type_1h": "machete",
            "type_2h": "polearm",
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

        zaw_link = zaws.ZawStrike.model_validate(props)
        assert zaw_link.model_dump() == props

    def test_create_zaw_strike_with_optional_fields(self):
        props = {
            "name": "Plague Kripath",
            "img_url": "",
            "type_1h": "rapier",
            "type_2h": "polearm",
            "base_damage": 213.0,
            "impact_damage": 30.0,
            "puncture_damage": 70.0,
            "slash_damage": 49.0,
            "viral_damage": 64.0,
            "speed": "+0.033",
            "critical_chance": "22%",
            "critical_multiplier": 2.2,
            "status": "18%",
            "riven_disposition": 0.6,
        }
        zaw_link = zaws.ZawStrike.model_validate(props)
        assert zaw_link.model_dump() == props
