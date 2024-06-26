from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from uvicorn import run

from swagger_splitter.admin.router import router as admin_router
from swagger_splitter.openapi_splitter import form_openapi
from swagger_splitter.site.router import router as site_router

app = FastAPI()

app.include_router(admin_router, tags=["Admin"])
app.include_router(site_router, tags=["Site"])


@app.get("/docs/admin", include_in_schema=False)
def get_admin_docs():
    return get_swagger_ui_html(
        openapi_url="/admin-openapi.json",
        title="Admin endpoints",
    )


@app.get("/docs/site", include_in_schema=False)
def get_admin_docs():
    return get_swagger_ui_html(
        openapi_url="/site-openapi.json",
        title="Site endpoints",
    )


@app.get("/admin-openapi.json", include_in_schema=False)
def get_admin_openapi_json():
    return form_openapi(
        app=app,
        title="Some title",
        version="8.800.555.35.35",
        summary="Awesome summary",
        description="Best description",
        tag="Admin",
    )


@app.get("/site-openapi.json", include_in_schema=False)
def get_admin_openapi_json():
    return form_openapi(
        app=app,
        title="Some title",
        version="8.800.555.35.35",
        summary="Awesome summary",
        description="Best description",
        tag="Site",
    )


run(app=app, host="0.0.0.0", port=3010)
