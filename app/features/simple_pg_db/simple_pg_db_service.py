from __future__ import annotations

from typing import Any, Dict, List

from sqlalchemy import select, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.engine import Connection
from sqlalchemy.orm import Session

from .simple_pg_db_models import SimplePgDbItem
from .simple_pg_db_schemas import CreateSimplePgDbItemRequest


class SimplePgDbNotFoundError(Exception):
    pass


class SimplePgDbDatabaseError(Exception):
    pass


class SimplePgDbOrmService:
    def create_item(self, db: Session, payload: CreateSimplePgDbItemRequest) -> SimplePgDbItem:
        try:
            item = SimplePgDbItem(name=payload.name.strip())
            db.add(item)
            db.commit()
            db.refresh(item)
            return item
        except SQLAlchemyError as exc:
            db.rollback()
            raise SimplePgDbDatabaseError("Database error while creating item") from exc

    def get_item(self, db: Session, item_id: int) -> SimplePgDbItem:
        item = db.get(SimplePgDbItem, item_id)
        if item is None:
            raise SimplePgDbNotFoundError(f"Item {item_id} not found")
        return item

    def list_items(self, db: Session) -> List[SimplePgDbItem]:
        statement = select(SimplePgDbItem).order_by(SimplePgDbItem.id)
        return list(db.scalars(statement).all())


class SimplePgDbSqlService:
    def create_item(self, connection: Connection, payload: CreateSimplePgDbItemRequest) -> Dict[str, Any]:
        try:
            result = connection.execute(
                text(
                    """
                    INSERT INTO simple_pg_db_items (name)
                    VALUES (:name)
                    RETURNING id, name, created_at
                    """
                ),
                {"name": payload.name.strip()},
            )
            row = result.mappings().one()
            return dict(row)
        except SQLAlchemyError as exc:
            raise SimplePgDbDatabaseError("Database error while creating item") from exc

    def get_item(self, connection: Connection, item_id: int) -> Dict[str, Any]:
        try:
            result = connection.execute(
                text(
                    """
                    SELECT id, name, created_at
                    FROM simple_pg_db_items
                    WHERE id = :item_id
                    """
                ),
                {"item_id": item_id},
            )
            row = result.mappings().first()
            if row is None:
                raise SimplePgDbNotFoundError(f"Item {item_id} not found")
            return dict(row)
        except SQLAlchemyError as exc:
            raise SimplePgDbDatabaseError("Database error while fetching item") from exc

    def list_items(self, connection: Connection) -> List[Dict[str, Any]]:
        try:
            result = connection.execute(
                text(
                    """
                    SELECT id, name, created_at
                    FROM simple_pg_db_items
                    ORDER BY id
                    """
                )
            )
            return [dict(row) for row in result.mappings().all()]
        except SQLAlchemyError as exc:
            raise SimplePgDbDatabaseError("Database error while listing items") from exc
