import math
from json_parser import (CompleteWeatherInfo1, parse_1_json)
from models.MessageInfo import MessageInfo

def scale_temperature(temp: int) -> int:   
    
    return round(temp - 273.15, 2)


def convert_to_string_and_add_units(val: int, unit: str)->str:
    str_val = str(val) + unit

    return str_val


def add_units(obj: CompleteWeatherInfo1) -> MessageInfo:
    message_info = MessageInfo()

    message_info.temp       = convert_to_string_and_add_units(obj.main.temp, " °C")
    message_info.feels_like = convert_to_string_and_add_units(obj.main.feels_like, " °C")
    message_info.temp_min   = convert_to_string_and_add_units(obj.main.temp_min,  " °C")
    message_info.temp_max   = convert_to_string_and_add_units(obj.main.temp_max, " °C")
    message_info.pressure = convert_to_string_and_add_units(obj.main.pressure, "mbar")
    message_info.humidity   = convert_to_string_and_add_units(obj.main.humidity, " %")
    message_info.wind_speed      = convert_to_string_and_add_units(obj.wind.speed, " m/s")

    return message_info


def kelvins_to_degrees(obj:CompleteWeatherInfo1) -> CompleteWeatherInfo1:
    obj.main.temp       = scale_temperature(obj.main.temp)
    obj.main.feels_like = scale_temperature(obj.main.feels_like)
    obj.main.temp_min   = scale_temperature(obj.main.temp_min)
    obj.main.temp_max   = scale_temperature(obj.main.temp_max)

    return obj

if __name__ == "__main__":
    pass
