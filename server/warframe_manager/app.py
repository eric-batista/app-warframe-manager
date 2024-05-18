import fastapi
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse

from warframe_manager.zaws.application.app import app as zaws_router

ROUTER_PREFIX = "/warframe-manager"


def get_application():
    origins = [
        "http://localhost",
        "http://localhost:8080",
        "https://eric-batista.github.com",
    ]

    application = fastapi.FastAPI(
        default_response_class=ORJSONResponse,
        docs_url=f"{ROUTER_PREFIX}/docs",
        redoc_url=f"{ROUTER_PREFIX}/redoc",
        openapi_url=f"{ROUTER_PREFIX}/openapi.json",
    )
    router = fastapi.APIRouter(prefix=ROUTER_PREFIX)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )

    router.include_router(zaws_router)
    application.include_router(router)

    return application


app = get_application()
