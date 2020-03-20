import json
from pydantic import BaseModel
from typing import List

class Coord(BaseModel):
    lon : float = None
    lat : float = None

class Weather_Info(BaseModel):
    id          : int = None
    main        : str = None
    description : str = None
    icon        : str = None

class Main(BaseModel):
    temp       : float = None
    feels_like : float = None
    temp_min   : float = None
    temp_max   : float = None
    pressure   : float = None
    humidity   : float = None

class Wind(BaseModel):
    speed : float = None
    deg   : float = None


class Complete_Weather_Info(BaseModel):
    coord      : Coord
    weather    : List[Weather_Info]
    main       : Main
    wind       : Wind

def parse_json(JSON):
    weather_info = Complete_Weather_Info.parse_obj(JSON)
    return weather_info

if __name__ == "__main__":
    pass