import typing
from uuid import UUID
from decimal import Decimal
from datetime import datetime
from pydantic import BaseModel, Field
from utilities.validation.types import Base64DecodedJSON, BinaryBoolType


class SensorRecordSchema(BaseModel):
    device_id: int = Field(validation_alias="v0")
    is_in_cell: BinaryBoolType = Field(validation_alias="v11")
    dwell_time: typing.Optional[Decimal] = Field(validation_alias="v18")
    timestamp: datetime = Field(validation_alias="Time")


class SensorRecordWrapperSchema(BaseModel):
    data: Base64DecodedJSON[SensorRecordSchema]


class SensorRecordRequestWrapperSchema(BaseModel):
    message: SensorRecordWrapperSchema


class SensorRecordReadSchema(SensorRecordSchema):
    id: UUID
    device_id: int = Field()
    is_in_cell: BinaryBoolType = Field()
    dwell_time: typing.Optional[Decimal] = Field()
    timestamp: datetime = Field()
