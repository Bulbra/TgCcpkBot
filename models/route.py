from datetime import datetime
from pydantic import BaseModel
from models.station import Station
from typing import Optional, Any


class Route(BaseModel):
    originStation: Station
    departureDateTime: datetime
    destinationStation: Station
    arrivalDateTime: datetime
    initialStation: Station
    finalStation: Station
    trainNumber: str
    displayTrainNumber: Optional[str] = None
    couponInfo: Optional[object] = None
    citizenshipRequired: bool
