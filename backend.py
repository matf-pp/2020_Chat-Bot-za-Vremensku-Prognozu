from urllib.parse import urljoin
import requests
import os
from dotenv import load_dotenv
from json_parser import (CompleteWeatherInfo, parse_1_json)
from scaling_and_conversion import (scale_temperature, convert_to_string_and_add_units, add_units, kelvins_to_degrees)
load_dotenv()

KEY = os.getenv("KEY")
URL1 = os.getenv("URL1")
URLL = os.getenv("URLL")

def make_request(req: str) -> CompleteWeatherInfo:
    res                = requests.get(req)
    print(res.json())
    weather_obj        = parse_1_json(res.json())
    
    return weather_obj


def get_readable_weather(obj: CompleteWeatherInfo) -> object:
    weather_obj_scaled = kelvins_to_degrees(obj)

    return add_units(weather_obj_scaled)


def get_by_city_name(params: str) -> CompleteWeatherInfo:
    city_name   = params
    req         = urljoin(URL1, f"?q={city_name}&appid={KEY}")    
    weather_obj = make_request(req)

    return get_readable_weather(weather_obj)


def get_by_lat_lon(params: tuple) -> CompleteWeatherInfo:
    lat, lon    = params
    req         = urljoin(URL1, f"?lat={lat}&lon={lon}&appid={KEY}")
    weather_obj = make_request(req)
    
    return get_readable_weather(weather_obj)


def get_by_city_id(params: int) -> CompleteWeatherInfo:
    city_id     = params
    req         = urljoin(URL1, f"?id={city_id}&appid={KEY}")
    weather_obj = make_request(req)

    return get_readable_weather(weather_obj)


def get_by_zip_code(params: tuple) -> CompleteWeatherInfo:
    zip_code, country_code = params
    req                    = urljoin(URL1, f"?zip={zip_code},{country_code}&appid={KEY}")
    weather_obj            = make_request(req)

    return get_readable_weather(weather_obj)


def get_by_multiple_lon_lat(params: tuple):
    lon_left, lat_bottom, lon_right, lat_top, zoom = params
    req                                            = urljoin(URLL, f"city?bbox={lon_left},{lat_bottom},{lon_right},{lat_top},{zoom}&appid={KEY}")
    weather_obj                                    = make_request(req)
    return weather_obj


if __name__ == "__main__":
    pass
