from typing import Optional, Any

from beanie import Document
from pydantic import BaseModel

class User(Document):
    fullname: str
    email: str
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "fullname": "Sayali Dalvi",
                "email": "dalvi.sa@northeastern.edu",
                "password": "sayali",
            }
        }

    class Settings:
        name = "user"

class UserData(BaseModel):
    fullname: Optional[str]
    email: Optional[str]
    password: Optional[str]
