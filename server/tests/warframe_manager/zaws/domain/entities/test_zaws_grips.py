from warframe_manager.zaws.domain.entities import zaws


class TestZawAssemble:
    def test_create_zaw_assemble(self):
        props = {
            "name": "Jayap",
            "img_url": "",
            "grip_type": "two-handed",
            "damage_bonus": "0",
            "base_speed": 0.917,
        }
        zaw_link = zaws.ZawGrip.model_validate(props)
        assert zaw_link.model_dump() == props
