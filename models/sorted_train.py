from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from models.image import Image
from models.route import Route
from models.comfort_option import ComfortOption
from models.place_quantity import PlaceQuantity


class SortedTrain(BaseModel):
    hasElectronicRegistration: bool
    hasTwoStoreyCars: bool
    carriers: list[str]
    trainNumber: str
    trainNumberToGetRoute: str
    displayTrainNumber: str
    trainDescription: str
    trainName: str
    originName: str
    originStationCode: str
    destinationName: str
    destinationStationCode: str
    initialStationName: str
    initialStationCode: str
    finalStationName: str
    finalStationCode: str
    departureDateTime: datetime
    localDepartureDateTime: datetime
    arrivalDateTime: datetime
    localArrivalDateTime: datetime
    departureDateFromFormingStation: datetime
    departureStopTime: int
    arrivalStopTime: int
    tripDuration: int
    tripDistance: int
    isSuburban: bool
    carServices: list[object]

    route: Route
    comfortOptionsSummary: list[ComfortOption]
    placeQuantity: PlaceQuantity
    images: Optional[list[Image]] = None
