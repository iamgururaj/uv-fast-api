from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class CreateFeature1Request(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)


class Feature1Response(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    created_at: datetime


class Feature1ListResponse(BaseModel):
    items: List[Feature1Response]
    total: int
