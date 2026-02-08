from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status

from .feature_1_schemas import CreateFeature1Request, Feature1ListResponse, Feature1Response
from .feature_1_service import Feature1NotFoundError, Feature1Service

router = APIRouter(prefix="/feature-1", tags=["feature-1"])

_service = Feature1Service()


def get_feature_1_service() -> Feature1Service:
    return _service


@router.post(
    "/",
    response_model=Feature1Response,
    status_code=status.HTTP_201_CREATED,
)
async def create_feature_1(
    payload: CreateFeature1Request,
    service: Feature1Service = Depends(get_feature_1_service),
) -> Feature1Response:
    return service.create_item(payload)


@router.get("/{item_id}", response_model=Feature1Response)
async def get_feature_1(
    item_id: int,
    service: Feature1Service = Depends(get_feature_1_service),
) -> Feature1Response:
    try:
        return service.get_item(item_id)
    except Feature1NotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc


@router.get("/", response_model=Feature1ListResponse)
async def list_feature_1(
    service: Feature1Service = Depends(get_feature_1_service),
) -> Feature1ListResponse:
    items = service.list_items()
    return Feature1ListResponse(items=items, total=len(items))
