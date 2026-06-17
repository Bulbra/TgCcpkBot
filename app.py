from models.sorted_train import SortedTrain
from models.train_places import TrainPlacesObject
from models.unsorted_train import UnsortedTrain
import requests
from pprint import pprint, pp
from datetime import datetime, date


def get_all_trains(
        from_station_id: int, to_station_id: int, origin_date: date) -> list[UnsortedTrain]:
    url = "https://backend.cppktrain.ru/train-schedule/date-travel"
    params = {
        "date": origin_date,
        "fromStationId": from_station_id,
        "toStationId": to_station_id
    }
    r = requests.get(url, params=params)
    result: list[UnsortedTrain] = []
    for train_dict in r.json():
        result.append(UnsortedTrain.model_validate(train_dict))
    return result


def get_all_free_trains(
        from_station_id: int, to_station_id: int, origin_date: date) -> list[SortedTrain]:
    url = "https://backend.cppktrain.ru/api/TrainPricing"
    params = {
        "departureDate": origin_date.strftime("%Y-%m-%d"),
        "originCode": from_station_id,
        "destinationCode": to_station_id
    }
    r = requests.get(url, params=params)
    result: list[SortedTrain] = []
    for train_dict in r.json():
        result.append(SortedTrain.model_validate(train_dict))
    return result


def get_all_train_places(
        train_id: str, from_station_id: str, to_station_id: str, origin_date: date) -> TrainPlacesObject:
    url = "https://backend.cppktrain.ru/api/CarPricing"
    params = {
        "departuredate": origin_date,
        "origincode": from_station_id,
        "destinationcode": to_station_id,
        "trainnumber": train_id
    }
    r = requests.get(url, params=params)
    return TrainPlacesObject.model_validate(r.json())
