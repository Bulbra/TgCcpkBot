from pydantic import BaseModel


class Places(BaseModel):
    top: int
    bottom: int
    total: int


class PlaceQuantity(BaseModel):
    count: int
    lower: int
    upper: int
    lowerSide: int
    upperSide: int
    male: int
    female: int
    emptyCabin: int
    mixedCabin: int
    minPrice: float
    maxPrice: float
    totalCount: int
