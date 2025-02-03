from uuid import UUID
from typing import Optional
from datetime import datetime
from fastapi import APIRouter, Depends
from fastapi_pagination import Page
from services.cell_sensors import CellSensorsService
from schemas.cell_sensors import SensorRecordRequestWrapperSchema, SensorRecordReadSchema


router = APIRouter()


@router.get("/sensors/data", response_model=Page[SensorRecordReadSchema])
async def sensors_data(
    service: CellSensorsService = Depends(),
    device_id: Optional[int] = None,
    timestamp__gt: Optional[datetime] = None,
    timestamp__lt: Optional[datetime] = None,
    is_in_cell: Optional[bool] = None,
) -> Page[SensorRecordReadSchema]:
    return await service.get_sensor_records(device_id, timestamp__gt, timestamp__lt, is_in_cell)


@router.post("/sensors/data/insert", response_model=SensorRecordReadSchema)
async def sensors_data_insert(data: SensorRecordRequestWrapperSchema, service: CellSensorsService = Depends()):
    return await service.insert_sensor_record(data)


@router.get("/sensors/data/{record_id}", response_model=SensorRecordReadSchema)
async def get_sensor_record(record_id: UUID, service: CellSensorsService = Depends()):
    return await service.get_sensor_record(record_id)
