import uuid
from fastapi import APIRouter, HTTPException, status
from app.schemas import IssueCreate , IssueOut ,IssueUpdate
from app.storage  import load_data , save_data


router = APIRouter(prefix="/api/v1/issues", tags=["Issues"])

@router.get("/" ,response_model=list[IssueOut])
async def get_issues():
    issues = load_data()
    return issues   


    @router.post("", response_model=IssueOut, status_code=status.HTTP_201_CREATED)
def create_issue(payload: IssueCreate):
    """
    Create new issue
    The issue is persisted to data/issues.json
    """
    issues = load_data()

    issue = {
        "id": str(uuid.uuid4()),
        "title": payload.title,
        "description": payload.description,
        "priority": payload.priority.value,
        "status": "open",
    }

    issues.append(issue)
    save_data(issues)

    return issue
