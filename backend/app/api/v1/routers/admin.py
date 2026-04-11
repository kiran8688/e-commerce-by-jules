from fastapi import APIRouter, Depends

from app.api.v1.deps import get_current_active_admin

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/dashboard", dependencies=[Depends(get_current_active_admin)])
def get_dashboard_summary():
    return {"message": "Admin dashboard functionality"}
