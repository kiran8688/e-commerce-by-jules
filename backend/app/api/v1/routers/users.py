from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me")
def get_current_user():
    return {"message": "Current user functionality"}
