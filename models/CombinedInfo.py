
from typing import Union
from . import (CityInCircleWeather, ManyCitiesWeather, OneCityWeather)



CombinedInfo = Union[
    CityInCircleWeather.WeatherInfo, 
    ManyCitiesWeather.WeatherInfo, 
    OneCityWeather.CompleteWeatherInfo
]

