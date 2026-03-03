from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional

class IssuesStatus(str, Enum):
    open = "open"
    in_progress = "in_progress"
    closed = "closed"


class IssuesPriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


    class IssueCreate(BaseModel):
        tittle: str = Field(..., min_length=5, max_length=100)
        description: [str] = Field(None, min_length=10, max_length=500)
        priority: IssuesPriority = IssuesPriority.medium
        

class IssueUpdate(BaseModel):
    title: Optional[str] = Filed(default=None, min_length=5, max_length=100)
    description: Optional[str] = Field(default=None, min_length=10, max_length=500)
    priority: Optional[IssuesPriority] = None 
    status: Optional[IssuesStatus] = None

class IssueOut(BaseModel):
    id : str
    tittle: str
    description: str
    priority: IssuesPriority
    status: IssuesStatus       
