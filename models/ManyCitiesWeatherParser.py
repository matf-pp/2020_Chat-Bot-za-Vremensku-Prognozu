from pydantic import BaseModel
from typing import List
from models.OneCityWeatherParser import (MainInfo, Wind, Coord)


class WeatherInfo(BaseModel):
    coord : Coord    = None
    main  : MainInfo = None
    wind  : Wind     = None
    name  : str      = None


class CompleteWeatherInfoM(BaseModel):
    cnt: int = None
    list : List[WeatherInfo]


