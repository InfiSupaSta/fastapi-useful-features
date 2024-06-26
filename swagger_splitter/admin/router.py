from typing import Literal

from fastapi import APIRouter

from swagger_splitter.admin.schemas import AdminModel

router = APIRouter(prefix="/admin")


@router.post("/admin-stuff")
def get_hostname(model: AdminModel) -> dict[Literal["status", "model"], str]:
    return {"status": "Admin", "model": model.something}
