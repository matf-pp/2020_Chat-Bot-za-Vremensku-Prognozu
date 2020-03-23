from urllib.parse import urljoin
import requests
import os
from dotenv import load_dotenv
from json_parser import (CompleteWeatherInfo, parse_json)

load_dotenv()

KEY = os.getenv("KEY")
URL = os.getenv("URL")


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

    obj.main.humidity   = convert_to_string_and_add_units(obj.main.humidity, " %")
    obj.wind.speed      = convert_to_string_and_add_units(obj.wind.speed, " m/s")

    return obj


def kelvins_to_degrees(obj:CompleteWeatherInfo) -> CompleteWeatherInfo:
    obj.main.temp       = scale_temperature(obj.main.temp)
    obj.main.feels_like = scale_temperature(obj.main.feels_like)
    obj.main.temp_min   = scale_temperature(obj.main.temp_min)
    obj.main.temp_max   = scale_temperature(obj.main.temp_max)

    return obj


def make_request(req: str) -> CompleteWeatherInfo:
    res                = requests.get(req)
    weather_obj        = parse_json(res.json())
    
    return weather_obj


def get_readable_weather(obj: CompleteWeatherInfo) -> object:
    weather_obj_scaled = kelvins_to_degrees(obj)

    return add_units(weather_obj_scaled)


def get_by_city_name(params: str) -> CompleteWeatherInfo:
    city_name   = params
    req         = urljoin(URL, f"?q={city_name}&appid={KEY}")    
    weather_obj = make_request(req)
    
    return get_readable_weather(weather_obj)
   

def get_by_lat_lon(params: tuple) -> CompleteWeatherInfo:
    lat, lon    = params
    req         = urljoin(URL, f"?lat={lat}&lon={lon}&appid={KEY}")
    weather_obj = make_request(req)
    
    return get_readable_weather(weather_obj)
    
if __name__ == "__main__":
    pass