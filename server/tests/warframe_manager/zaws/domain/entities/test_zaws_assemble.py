from warframe_manager.zaws.domain.entities import zaws


class TestZaws:
    def test_create_assembled_zaw(self):
        props = {
            "name": "Jayap",
            "img_url": "",
            "grip_type": "two-handed",
            "damage_bonus": "0",
            "base_speed": 0.917,
        }
        zaw_grip = zaws.ZawGrip.model_validate(props)

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

        zaw_strike = zaws.ZawStrike.model_validate(props)

        props = {
            "name": "Vargeet Jai",
            "img_url": "",
            "speed_bonus": "+0.083",
            "critical_chance": "+7%",
            "status_chance": "-4%",
            "damage_bonus": "-4",
        }
        zaw_link = zaws.ZawLink.model_validate(props)

        props = {
            "name": "Zaw",
            "strike": zaw_strike.model_dump(),
            "grip": zaw_grip.model_dump(),
            "link": zaw_link.model_dump(),
            "level": "0",
            "gild": False,
        }

        zaw = zaws.Zaw.model_validate(props)
        assert zaw.model_dump() == props

        total_damage = zaw.calculate_total_damage()
        assert total_damage == 230.0 * 1.07

        total_crit_chance = zaw.calculate_total_critical_chance()
        assert total_crit_chance == 7 + 18

        parts_name = zaw.get_parts_name()
        assert parts_name == "Kronsh + Jayap + Vargeet Jai"

        total_speed = zaw.calculate_total_attack_speed()
        assert total_speed == 0.083 - 0.067 + 0.917

        total_status = zaw.calculate_total_status_chance()
        assert total_status == -4.0 + 18
