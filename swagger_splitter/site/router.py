from typing import Literal

from fastapi import APIRouter

from swagger_splitter.site.schemas import SiteModel

router = APIRouter(prefix="/site")


@router.post("/site-stuff")
def get_hostname(model: SiteModel) -> dict[Literal["status", "model"], str]:
    return {"status": "Site", "model": model.something}
