from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from models.comfort_option import ComfortOption


class UnsortedTrain(BaseModel):
    cost: float
    tariffId: int
    trainNumber: str
    startTime: datetime
    startStationId: int
    startStationName: str
    startStationLatinName: str
    finishTime: datetime
    finishStationId: int
    finishStationName: str
    finishStationLatinName: str
    departureStationId: int
    departureStationName: str
    departureStationLatinName: str
    departureStationHasWicket: bool
    arrivalStationId: int
    arrivalStationName: str
    arrivalStationLatinName: str
    arrivalStationHasWicket: bool
    defaultDirection: bool
    departureTime: datetime
    arrivalTime: datetime
    scheduleId: int
    motionMode: str
    trainCategoryId: int
    rzdTrainCategoryId: int
    mcd: Optional[str] = None
    canceled: Optional[bool] = None
    deviation: Optional[bool] = None
    shortCarrier: str
    carriers: list[str]
    comfortOptionsSummary: list[ComfortOption]
    transfer: Optional[bool] = None
