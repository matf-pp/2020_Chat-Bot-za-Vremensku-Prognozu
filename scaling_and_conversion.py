import math
from json_parser import (CompleteWeatherInfo, parse_1_json)


def scale_temperature(temp: int) -> int:   
    
    return round(temp - 273.15, 2)


def convert_to_string_and_add_units(val: int, unit:str)->str:
    str_val = str(val) + unit

    return str_val


def add_units(obj: CompleteWeatherInfo) -> object:
    obj.main.temp       = convert_to_string_and_add_units(obj.main.temp, " °C")
    obj.main.feels_like = convert_to_string_and_add_units(obj.main.feels_like, " °C")
    obj.main.temp_min   = convert_to_string_and_add_units(obj.main.temp_min,  " °C")
    obj.main.temp_max   = convert_to_string_and_add_units(obj.main.temp_max, " °C")
    obj.main.pressure = convert_to_string_and_add_units(obj.main.pressure, "mbar")
    obj.main.humidity   = convert_to_string_and_add_units(obj.main.humidity, " %")
    obj.wind.speed      = convert_to_string_and_add_units(obj.wind.speed, " m/s")

    return obj


def kelvins_to_degrees(obj:CompleteWeatherInfo) -> CompleteWeatherInfo:
    obj.main.temp       = scale_temperature(obj.main.temp)
    obj.main.feels_like = scale_temperature(obj.main.feels_like)
    obj.main.temp_min   = scale_temperature(obj.main.temp_min)
    obj.main.temp_max   = scale_temperature(obj.main.temp_max)

    return obj

if __name__ == "__main__":
    pass