from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import BigInteger, DECIMAL

from utilities.database.models import Base
from utilities.database.types import TZDateTime


class SensorRecord(Base):
    __tablename__ = 'sensor_records'
    device_id: Mapped[int] = mapped_column(BigInteger, index=True, nullable=False)
    is_in_cell: Mapped[bool] = mapped_column(nullable=False)
    dwell_time = mapped_column(DECIMAL, nullable=True)
    timestamp: Mapped[datetime] = mapped_column(TZDateTime, nullable=False)
