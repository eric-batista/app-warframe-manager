import fastapi

from warframe_manager.zaws.application.dtos import zaws as dto_models
from warframe_manager.zaws.domain.entities import zaws as domain_models
from warframe_manager.zaws.infra.adapters.database import get_database_adapter
from warframe_manager.zaws.infra.core.settings import BASE_PATH

from . import usecases

app = fastapi.APIRouter(prefix=BASE_PATH)


@app.post("")
def create_zaw(payload: dto_models.ZawRequest = fastapi.Body()):
    return usecases.RegisterZaw(
        zaw=payload, database_adapter=get_database_adapter()
    ).execute()


@app.post("/link")
def create_zaw_link(payload: domain_models.ZawLink = fastapi.Body()):
    return usecases.RegisterZawLink(
        zaw=payload, database_adapter=get_database_adapter()
    ).execute()


@app.post("/grip")
def create_zaw_grip(payload: domain_models.ZawGrip = fastapi.Body()):
    return usecases.RegisterZawGrip(
        zaw=payload, database_adapter=get_database_adapter()
    ).execute()


@app.post("/strike")
def create_zaw_link(
    payload: domain_models.ZawStrike = fastapi.Body(),
):
    return usecases.RegisterZawStrike(
        zaw=payload, database_adapter=get_database_adapter()
    ).execute()
