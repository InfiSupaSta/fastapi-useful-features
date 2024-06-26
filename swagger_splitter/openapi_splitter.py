from typing import Any

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.routing import APIRoute


def form_openapi(
    *,
    app: FastAPI,
    title: str,
    version: str,
    summary: str,
    description: str,
    tag: str,
) -> Any:
    """Формирует openapi спецификацию для swagger только с эндпоинтами, которые имеют определённый tag."""
    return get_openapi(
        title=title,
        version=version,
        summary=summary,
        description=description,
        routes=[
            route for route in app.routes
            if isinstance(route, APIRoute)
            and tag in route.tags
        ],
    )
