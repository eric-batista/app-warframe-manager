from warframe_manager.zaws.domain.entities import zaws


class TestZawLinks:
    def test_create_zaw_link_without_optional_fields(self):
        props = {
            "name": "Jai",
            "img_url": "",
            "speed_bonus": "+0.083",
            "critical_chance": None,
            "status_chance": None,
            "damage_bonus": "-4",
        }
        zaw_link = zaws.ZawLink.model_validate(props)
        assert zaw_link.model_dump() == props

    def test_create_zaw_link_with_optional_fields(self):
        props = {
            "name": "Vargeet Jai",
            "img_url": "",
            "speed_bonus": "+0.083",
            "critical_chance": "+7%",
            "status_chance": "-4%",
            "damage_bonus": "-4",
        }
        zaw_link = zaws.ZawLink.model_validate(props)
        assert zaw_link.model_dump() == props
