from pydantic import BaseModel
from typing import List


class Coord(BaseModel):
    lon : float = None
    lat : float = None

        
class WeatherInfo(BaseModel):
    id          : int = None
    main        : str = None
    description : str = None
    icon        : str = None

        
class MainInfo(BaseModel):
    temp       : float = None
    feels_like : float = None
    temp_min   : float = None
    temp_max   : float = None
    pressure   : float = None
    humidity   : float = None

        
class Wind(BaseModel):
    speed : float = None
    deg   : float = None
        

class CompleteWeatherInfo(BaseModel):
    coord      : Coord
    weather    : List[WeatherInfo]
    main       : MainInfo
    wind       : Wind