from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/issues", tags=["Issues"])

@router.get("/")
async def get_issues():
    return []