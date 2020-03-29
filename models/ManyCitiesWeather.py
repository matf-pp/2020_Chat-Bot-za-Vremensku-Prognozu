from pydantic import BaseModel
from typing import List
from models.OneCityWeather import (MainInfo, Wind, Coord)


class WeatherInfo(BaseModel):
    coord : Coord    = None
    main  : MainInfo = None
    wind  : Wind     = None
    name  : str      = None


class CompleteWeatherInfo(BaseModel):
    cod     : int = None
    message : str = None
    cnt     : int = None
    list    : List[WeatherInfo] = None


