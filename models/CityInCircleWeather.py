from pydantic import BaseModel
from typing import List
from models.OneCityWeather import (Coord, MainInfo)
import requests

class Wind(BaseModel):
    speed: int

class WeatherInfo(BaseModel):
    name    : str      = None
    coord   : Coord    = None
    main    : MainInfo = None
    wind    : Wind     = None

class CompleteWeatherInfo(BaseModel):
    cod   : str
    count : int
    list  : List[WeatherInfo] 

if __name__ == "__main__":
    pass
