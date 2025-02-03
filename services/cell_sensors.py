from uuid import UUID
from typing import Optional
from datetime import datetime
from fastapi import Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.database import get_db
from schemas.cell_sensors import SensorRecordRequestWrapperSchema
from models.cell_sensors import SensorRecord


class CellSensorsService:
    def __init__(self, session: AsyncSession = Depends(get_db)):
        self.session = session

    async def insert_sensor_record(self, data: SensorRecordRequestWrapperSchema):
        sensor_record = SensorRecord(**data.message.data.model_dump())
        self.session.add(sensor_record)
        await self.session.commit()
        await self.session.refresh(sensor_record)
        return sensor_record

    async def get_sensor_records(
        self,
        device_id: Optional[int] = None,
        timestamp__gt: Optional[datetime] = None,
        timestamp__lt: Optional[datetime] = None,
        is_in_cell: Optional[bool] = None,
    ):
        query = select(SensorRecord).order_by(SensorRecord.timestamp.asc())
        if device_id is not None:
            query = query.where(SensorRecord.device_id == device_id)
        if timestamp__gt is not None:
            query = query.where(SensorRecord.timestamp > timestamp__gt)
        if timestamp__lt is not None:
            query = query.where(SensorRecord.timestamp < timestamp__lt)
        if is_in_cell is not None:
            query = query.where(SensorRecord.is_in_cell == is_in_cell)
        return await paginate(self.session, query)

    async def get_sensor_record(self, record_id: UUID):
        query = select(SensorRecord).where(SensorRecord.id == record_id)
        result = await self.session.execute(query)
        record = result.scalar_one_or_none()
        if record is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return record
