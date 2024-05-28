import fastapi

from warframe_manager.kitguns.infra.core.settings import BASE_PATH

app = fastapi.APIRouter(prefix=BASE_PATH, tags=["Kitguns"])


@app.post("")
def create_kitgun():
    return


@app.post("/loader")
def create_kitgun_loader():
    return


@app.post("/chamber")
def create_kitgun_chamber():
    return


@app.post("/grip")
def create_kitgun_grip():
    return
