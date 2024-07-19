from fastapi import FastAPI

from application.api.user.handlers import router as user_router


def create_app() -> FastAPI:
    app = FastAPI(
        title='MediaApp',
        docs_url='/api/docs',
        debug=True
    )

    app.include_router(user_router, prefix='/user')

    return app
