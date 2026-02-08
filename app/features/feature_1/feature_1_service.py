from __future__ import annotations

from datetime import datetime, timezone
from threading import Lock
from typing import Dict, List

from .feature_1_schemas import CreateFeature1Request, Feature1Response


class Feature1NotFoundError(Exception):
    pass


class Feature1Service:
    def __init__(self) -> None:
        self._lock = Lock()
        self._items: Dict[int, Feature1Response] = {}
        self._next_id = 1

    def create_item(self, payload: CreateFeature1Request) -> Feature1Response:
        with self._lock:
            item_id = self._next_id
            self._next_id += 1

            item = Feature1Response(
                id=item_id,
                name=payload.name.strip(),
                description=payload.description,
                created_at=datetime.now(timezone.utc),
            )

            self._items[item_id] = item
            return item

    def get_item(self, item_id: int) -> Feature1Response:
        item = self._items.get(item_id)
        if item is None:
            raise Feature1NotFoundError(f"Item {item_id} not found")
        return item

    def list_items(self) -> List[Feature1Response]:
        return list(self._items.values())
