from pydantic import BaseModel
from typing import List
from models.OneCityWeatherParser import (MainInfo, Wind)


class Coord(BaseModel):
    Lon: float = None
    Lat: float = None


class WeatherInfo(BaseModel):
    name  : str      = None
    coord : Coord    = None
    main  : MainInfo = None
    wind  : Wind     = None


class CompleteWeatherInfoLL(BaseModel):
    cnt: int = None
    list: List[WeatherInfo] = []


