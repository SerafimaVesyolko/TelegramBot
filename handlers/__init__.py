from .custom import router as custom_router
from . import catalog

routers = [
    custom_router,
    catalog.router,
]