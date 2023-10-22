from typing import Optional, Any

from beanie import Document
from pydantic import BaseModel


class Report(Document):
    fullname: str
    email: str
    phone: str
    college_name: str
    issue_type: int
    location: float
    date: str
    description: str
    witnesses: str
    actions_taken: str
    additional_comments: str

    class Config:
        json_schema_extra = {
            "example": {
                "fullname": "Sayali Dalvi",
                "email": "dalvi.sa@northeastern.edu",
                "phone": "8573088727",
                "college_name": "College of Engineering",
                "issue_type": "Harassment",
                "location": "Elle Hall",
                "date": "08/08/2022",
                "description": "Harassment",
                "witnesses": "",
                "actions_taken": "",
                "additional_comments": "",
            }
        }

    class Settings:
        name = "report"


class Response(BaseModel):
    status_code: int
    response_type: str
    description: str
    data: Optional[Any]

    class Config:
        schema_extra = {
            "example": {
                "status_code": 200,
                "response_type": "success",
                "description": "Operation successful",
                "data": "Sample data",
            }
        }

class ReportData(BaseModel):
    fullname: str
    email: str
    phone: str
    college_name: str
    issue_type: str
    location: str
    date: str
    description: str
    witnesses: str
    actions_taken: str
    additional_comments: str

    class Config:
        json_schema_extra = {
            "example": {
                "fullname": "Sayali Dalvi",
                "email": "dalvi.sa@northeastern.edu",
                "phone": "8573088727",
                "college_name": "College of Engineering",
                "issue_type": "Harassment",
                "location": "Elle Hall",
                "date": "08/08/2022",
                "description": "Harassment",
                "witnesses": "",
                "actions_taken": "",
                "additional_comments": "",
            }
        }

