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
    title: str = Field(..., min_length=5, max_length=100)
    description: Optional[str] = Field(None, min_length=10, max_length=500)
    priority: IssuesPriority = IssuesPriority.medium
        

class IssueUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=5, max_length=100)
    description: Optional[str] = Field(default=None, min_length=10, max_length=500)
    priority: Optional[IssuesPriority] = None 
    status: Optional[IssuesStatus] = None

class IssueOut(BaseModel):
    id: str
    title: str
    description: str
    priority: IssuesPriority
    status: IssuesStatus