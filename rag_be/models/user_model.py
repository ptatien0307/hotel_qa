from uuid import UUID, uuid4
from pydantic import BaseModel, Field

class UserModel(BaseModel):
    user_id: UUID = Field(default_factory=uuid4, alias="_id")
    username: str = Field(default=None)
    password: str = Field(default=None)
    created_by: str = Field(default="Admin")
    created_at: str = Field(default=None)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "username": "username",
                "password": "password",
                "created_by": "Admin",
                "created_at": "2024-01-01 00:00:00",
            }
        }

class CreatedUserModel(BaseModel):
    username: str = Field(default=None)
    password: str = Field(default=None)
