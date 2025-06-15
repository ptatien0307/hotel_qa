from uuid import UUID, uuid4
from pydantic import BaseModel, Field

class SessionModel(BaseModel):
    session_id: UUID = Field(default_factory=uuid4, alias="_id")
    user_id: str = Field(default=None)
    history: list = Field(default=None)
    created_by: str = Field(default="Admin")
    created_at: str = Field(default=None)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "user_id": "user_id",
                "history": [],
                "created_by": "Admin",
                "created_at": "2024-01-01 00:00:00",
            }
        }


class UpdatedSessionModel(BaseModel):
    session_id: str = Field(default=None)
    history: list[str] = Field(default=None)
    class Config:
        json_schema_extra = {
            "example": {
                "session_id": '12345',
                "history": ["item1", "item2", 'item3', 'item4'],
            }
        }

class CreateSessionModel(BaseModel):
    user_id: str