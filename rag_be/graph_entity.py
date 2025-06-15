from typing import List
from langchain_core.pydantic_v1 import BaseModel, Field

class Entities(BaseModel):
    """
        Identifying information about entities.
    """

    names: List[str] = Field(
        ...,
        description="All entities that appear in the text",
    )