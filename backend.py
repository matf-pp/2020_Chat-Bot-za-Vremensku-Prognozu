from urllib.parse import urljoin
import requests
import os
from dotenv import load_dotenv
from json_parser import (CompleteWeatherInfo, parse_json)
from scaling_and_conversion import (scale_temperature, convert_to_string_and_add_units, add_units, kelvins_to_degrees)
load_dotenv()

KEY = os.getenv("KEY")
URL = os.getenv("URL")

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


def get_by_city_id(params: int) -> CompleteWeatherInfo:
    city_id     = params
    req         = urljoin(URL, f"?id={city_id}&appid={KEY}")
    weather_obj = make_request(req)

    return get_readable_weather(weather_obj)


def get_by_zip_code(params: tuple) -> CompleteWeatherInfo:
    zip_code, country_code = params
    req                    = urljoin(URL, f"?zip={zip_code},{country_code}&appid={KEY}")
    weather_obj            = make_request(req)

    return get_readable_weather(weather_obj)


if __name__ == "__main__":
    pass