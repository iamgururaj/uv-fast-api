from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.engine import Connection
from sqlalchemy.orm import Session

from app.core.database import get_connection, get_db

from .simple_pg_db_schemas import (
    CreateSimplePgDbItemRequest,
    SimplePgDbItemListResponse,
    SimplePgDbItemResponse,
)
from .simple_pg_db_service import (
    SimplePgDbDatabaseError,
    SimplePgDbNotFoundError,
    SimplePgDbOrmService,
    SimplePgDbSqlService,
)

router = APIRouter(prefix="/simple-pg-db", tags=["simple-pg-db"])

_orm_service = SimplePgDbOrmService()
_sql_service = SimplePgDbSqlService()


def get_orm_service() -> SimplePgDbOrmService:
    return _orm_service


def get_sql_service() -> SimplePgDbSqlService:
    return _sql_service


@router.post(
    "/orm",
    response_model=SimplePgDbItemResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_item_orm(
    payload: CreateSimplePgDbItemRequest,
    db: Session = Depends(get_db),
    service: SimplePgDbOrmService = Depends(get_orm_service),
) -> SimplePgDbItemResponse:
    try:
        return service.create_item(db, payload)
    except SimplePgDbDatabaseError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(exc),
        ) from exc


@router.get("/orm/{item_id}", response_model=SimplePgDbItemResponse)
async def get_item_orm(
    item_id: int,
    db: Session = Depends(get_db),
    service: SimplePgDbOrmService = Depends(get_orm_service),
) -> SimplePgDbItemResponse:
    try:
        return service.get_item(db, item_id)
    except SimplePgDbNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    except SimplePgDbDatabaseError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(exc),
        ) from exc


@router.get("/orm", response_model=SimplePgDbItemListResponse)
async def list_items_orm(
    db: Session = Depends(get_db),
    service: SimplePgDbOrmService = Depends(get_orm_service),
) -> SimplePgDbItemListResponse:
    try:
        items = service.list_items(db)
        return SimplePgDbItemListResponse(items=items, total=len(items))
    except SimplePgDbDatabaseError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(exc),
        ) from exc


@router.post(
    "/sql",
    response_model=SimplePgDbItemResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_item_sql(
    payload: CreateSimplePgDbItemRequest,
    connection: Connection = Depends(get_connection),
    service: SimplePgDbSqlService = Depends(get_sql_service),
) -> SimplePgDbItemResponse:
    try:
        return service.create_item(connection, payload)
    except SimplePgDbDatabaseError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(exc),
        ) from exc


@router.get("/sql/{item_id}", response_model=SimplePgDbItemResponse)
async def get_item_sql(
    item_id: int,
    connection: Connection = Depends(get_connection),
    service: SimplePgDbSqlService = Depends(get_sql_service),
) -> SimplePgDbItemResponse:
    try:
        return service.get_item(connection, item_id)
    except SimplePgDbNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    except SimplePgDbDatabaseError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(exc),
        ) from exc


@router.get("/sql", response_model=SimplePgDbItemListResponse)
async def list_items_sql(
    connection: Connection = Depends(get_connection),
    service: SimplePgDbSqlService = Depends(get_sql_service),
) -> SimplePgDbItemListResponse:
    try:
        items = service.list_items(connection)
        return SimplePgDbItemListResponse(items=items, total=len(items))
    except SimplePgDbDatabaseError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(exc),
        ) from exc
