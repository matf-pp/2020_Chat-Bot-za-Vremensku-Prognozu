import math
from models.MessageInfo import MessageInfo
from models import (CityInCircleWeather, ManyCitiesWeather, OneCityWeather)
from typing import Union

CONTAIN_ALL = Union[CityInCircleWeather.WeatherInfo, ManyCitiesWeather.WeatherInfo, OneCityWeather.CompleteWeatherInfo]

def scale_temperature(temp: int) -> int:   
    
    return round(temp - 273.15, 2)


def convert_to_string_and_add_units(val: int, unit: str)->str:
    str_val = str(val) + unit

    return str_val


def is_in_Kelvin(temp: float)->bool:

    return temp > 273.15


def readable_weather(obj: CONTAIN_ALL) -> MessageInfo:
    msg_info = MessageInfo()

    try:
        MainInfo = obj.main

        if is_in_Kelvin(MainInfo.temp):
            MainInfo.temp = scale_temperature(MainInfo.temp)
        if is_in_Kelvin(MainInfo.feels_like):
            MainInfo.feels_like = scale_temperature(MainInfo.feels_like)
        if is_in_Kelvin(MainInfo.temp_min):
            MainInfo.temp_min = scale_temperature(MainInfo.temp_min)
        if is_in_Kelvin(MainInfo.temp_max):
            MainInfo.temp_max = scale_temperature(MainInfo.temp_max)
        
        msg_info.temp       = convert_to_string_and_add_units(MainInfo.temp, " °C")
        msg_info.feels_like = convert_to_string_and_add_units(MainInfo.feels_like, " °C")
        msg_info.temp_min   = convert_to_string_and_add_units(MainInfo.temp_min, " °C")
        msg_info.temp_max   = convert_to_string_and_add_units(MainInfo.temp_max, " °C")
        msg_info.humidity   = convert_to_string_and_add_units(MainInfo.humidity, " %")
        msg_info.pressure   = convert_to_string_and_add_units(MainInfo.pressure, " mbar")
        msg_info.wind_speed = convert_to_string_and_add_units(obj.wind.speed, " m/s")
        msg_info.name       = obj.name

    except AttributeError:
        print("Attribute missing!")

    return msg_info


if __name__ == "__main__":
    pass
