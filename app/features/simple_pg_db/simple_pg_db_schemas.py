from __future__ import annotations

from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict, Field


class CreateSimplePgDbItemRequest(BaseModel):
    name: str = Field(min_length=1, max_length=100)


class SimplePgDbItemResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    created_at: datetime


class SimplePgDbItemListResponse(BaseModel):
    items: List[SimplePgDbItemResponse]
    total: int
