from fastapi import APIRouter

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/dashboard")
def get_dashboard_summary():
    return {"message": "Admin dashboard functionality"}
