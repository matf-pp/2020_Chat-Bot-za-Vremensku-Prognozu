from pydantic import BaseModel
from typing import List
from models.OneCityWeather import (Coord, MainInfo)
import requests

class Wind(BaseModel):
    speed: int = None

class WeatherInfo(BaseModel):
    name    : str      = None
    coord   : Coord    = None
    main    : MainInfo = None
    wind    : Wind     = None

class CompleteWeatherInfo(BaseModel):
    cod   : int = None
    message: str = None
    count : int = None
    list  : List[WeatherInfo] = None 

if __name__ == "__main__":
    pass
