import math
from models.MessageInfo import MessageInfo
from models.CombinedInfo import CombinedInfo
from models import (CityInCircleWeather, ManyCitiesWeather, OneCityWeather)
from typing import Union

def scale_temperature(temp: int) -> int:   
    
    return round(temp - 273.15, 2)


def convert_to_string_and_add_units(val: int, unit: str)->str:
    str_val = str(val) + unit

    return str_val


def is_in_Kelvin(temp: float)->bool:

    return temp > 273.15


def readable_weather(obj: CombinedInfo) -> MessageInfo:
    msg_info = MessageInfo()

    try:
        MainInfo = obj.main

        try:
            if is_in_Kelvin(MainInfo.temp):
                MainInfo.temp       = scale_temperature(MainInfo.temp)
                msg_info.temp       = convert_to_string_and_add_units(MainInfo.temp, " °C")
        except AttributeError:
            print("Field temp doesn't exist")

        try:
            if is_in_Kelvin(MainInfo.feels_like):
                MainInfo.feels_like = scale_temperature(MainInfo.feels_like)
                msg_info.feels_like = convert_to_string_and_add_units(MainInfo.feels_like, " °C")
        except AttributeError:
            print("Field feels_like doesn't exist")

        try:    
            if is_in_Kelvin(MainInfo.temp_min):
                MainInfo.temp_min = scale_temperature(MainInfo.temp_min)
                msg_info.temp_min = convert_to_string_and_add_units(MainInfo.temp_min, " °C")
        except AttributeError:
            print("Field temp_min doesn't exist")

        try:
            if is_in_Kelvin(MainInfo.temp_max):
                MainInfo.temp_max = scale_temperature(MainInfo.temp_max)
                msg_info.temp_max = convert_to_string_and_add_units(MainInfo.temp_max, " °C")
        except AttributeError:
            print("Field temp_max doesn't exist")

        
        try:
            msg_info.humidity   = convert_to_string_and_add_units(MainInfo.humidity, " %")
        except AttributeError:
            print("Field humidity doesn't exist")

        try:
            msg_info.pressure   = convert_to_string_and_add_units(MainInfo.pressure, " mbar")
        except AttributeError:
            print("Field pressure doesn't exist")

        try:
            msg_info.wind_speed = convert_to_string_and_add_units(obj.wind.speed, " m/s")
        except AttributeError:
            print("Field wind_speed doesn't exist")

        try:
            msg_info.name       = obj.name
        except AttributeError:
            print("Field name doesn't exist")

    except AttributeError:
        print("Attribute missing!")

    return msg_info


if __name__ == "__main__":
    pass
