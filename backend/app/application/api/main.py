from contextlib import asynccontextmanager

from fastapi import FastAPI

from application.api.user.handlers import router as user_router

from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
]


def create_app() -> FastAPI:
    app = FastAPI(
        title='MediaApp',
        docs_url='/api/docs',
        debug=True,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(user_router, prefix='/api/user')

    return app
