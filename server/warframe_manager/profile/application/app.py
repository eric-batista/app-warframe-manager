import fastapi

from warframe_manager.profile.infra.core.settings import BASE_PATH

from . import usecases

app = fastapi.APIRouter(prefix=BASE_PATH, tags=["Profile"])


@app.get("")
def hello():
    return
