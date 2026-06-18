from typing import Optional
from pydantic import BaseModel
from models.image import Image
from models.route import Route
from models.comfort_option import ComfortOption
from models.place_quantity import Places


class Cars(BaseModel):
    number: int
    seats: list[int]
    placeQuantity: int
    displaySeats: list[str]
    schemeName: str
    showScheme: bool
    schemeWarning: bool
    price: float
    carAttributes: Optional[dict[str, bool]] = None
    comfortOptions: list[ComfortOption]
    images: Optional[list[Image]] = None
    carWithoutPlaces: bool
    placeReservationType: str


class TrainPlace(BaseModel):
    serviceClass: str
    internationalServiceClass: Optional[str] = None
    carTypeName: str
    carType: str
    displayName: str
    displayCode: str
    description: str
    descriptionUrl: Optional[str] = None
    price: float
    places: Places
    cars: list[Cars]
    owner: Optional[dict[str, str]] = None
    images: Optional[list[Image]] = None


class TrainPlacesObject(BaseModel):
    trainRoute: Route
    trainPlaces: list[TrainPlace]
    images: Optional[list[Image]] = None
    captcha: Optional[dict[str, str]] = None
