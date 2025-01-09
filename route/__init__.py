from core.app import app
from const.route import DS
from . import auth
from . import user
from . import smart_scrapper

app.include_router(auth.router, prefix=f"{DS}/auth", tags=["auth"])

app.include_router(user.router, prefix=f"{DS}/user", tags=["user"])

app.include_router(smart_scrapper.router, prefix=f"{DS}/scrap", tags=["scrap"])
