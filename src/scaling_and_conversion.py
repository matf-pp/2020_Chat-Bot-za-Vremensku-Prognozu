import math
from models.MessageInfo import MessageInfo
from models.CombinedInfo import CombinedInfo
from models import (CityInCircleWeather, ManyCitiesWeather, OneCityWeather)
from models.OneCityWeather import MainInfo
from typing import Union


def is_in_Kelvin(temp: float)->bool:
    return temp > 273.15

def scale_temperature(temp: int) -> int:   
    if is_in_Kelvin(temp):
        return round(temp - 273.15, 2)
    else:
        return round(temp, 2)

def convert_temp_to_string_and_add_units(val, unit):
    str_val = str(scale_temperature(val)) + unit
    return str_val

def convert_to_string_and_add_units(val: int, unit: str)->str:
    str_val = str(val) + unit
    return str_val


def get_attribute_and_add_units(obj: Union[CombinedInfo, int], attribute:str,  units: str) -> Union[MainInfo, str, None]:
    attr = getattr(obj, attribute, None)
    if attr is None:
        return None
    
    elif units is None:
        return attr
    
    elif 'temp' in attribute:
        return convert_temp_to_string_and_add_units(attr, units)

    else:
        return convert_to_string_and_add_units(attr, units)


def readable_weather(obj: CombinedInfo) -> MessageInfo:
    msg_info = MessageInfo()
    MainInfo = get_attribute_and_add_units(obj, "main", None)

    if MainInfo == None:
        return None

    msg_info.temp = get_attribute_and_add_units(MainInfo, "temp", " °C")
    msg_info.feels_like = get_attribute_and_add_units(MainInfo, "feels_like", " °C")
    msg_info.temp_min = get_attribute_and_add_units(MainInfo, "temp_min", " °C")
    msg_info.temp_max = get_attribute_and_add_units(MainInfo, "temp_max", " °C")
    msg_info.humidity = get_attribute_and_add_units(MainInfo, "humidity", " %")
    msg_info.pressure = get_attribute_and_add_units(MainInfo, "pressure", " mbar")
    msg_info.wind_speed = get_attribute_and_add_units(MainInfo, "wind.speed", " m/s")
    msg_info.name = get_attribute_and_add_units(obj, "name", None)
    
    return msg_info


if __name__ == "__main__":
    pass
