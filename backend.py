from urllib.parse import urljoin
import requests
import os
from dotenv import load_dotenv
from json_parser import (CompleteWeatherInfo1, parse_1_json,
                         CompleteWeatherInfoLL, parse_ll_json,
                         CompleteWeatherInfoR, parse_r_json,
                         CompleteWeatherInfoM, parse_m_json)

from scaling_and_conversion import (scale_temperature, convert_to_string_and_add_units, add_units, kelvins_to_degrees)
from models.MessageInfo import MessageInfo
from typing import List

load_dotenv()

KEY = os.getenv("KEY")
URL = os.getenv("URL")

def make_request(req: str, CODE:int) -> CompleteWeatherInfo1:
    res                    = requests.get(req)
    if CODE == 0:
        weather_obj        = parse_1_json(res.json())
    elif CODE == 1:
        weather_obj        = parse_ll_json(res.json())
    elif CODE == 2:
        weather_obj        = parse_r_json(res.json())
    elif CODE == 3:
        weather_obj        = parse_m_json(res.json())
    
    return weather_obj


def get_readable_weather(obj: CompleteWeatherInfo1) -> MessageInfo:
    weather_obj_scaled = kelvins_to_degrees(obj)

    return add_units(weather_obj_scaled)


def get_by_city_name(params: str) -> MessageInfo:
    CODE        = 0
    city_name   = params
    req         = urljoin(URL, f"weather?q={city_name}&appid={KEY}")    

    weather_obj = make_request(req, CODE)
    return get_readable_weather(weather_obj)


def get_by_geographic_coordinates(params: tuple) -> MessageInfo:
    CODE        = 0
    lat, lon    = params
    req         = urljoin(URL, f"weather?lat={lat}&lon={lon}&appid={KEY}")
    weather_obj = make_request(req, CODE)
    
    return get_readable_weather(weather_obj)


def get_by_city_id(params: int) -> MessageInfo:
    CODE        = 0
    city_id     = params
    req         = urljoin(URL, f"weather?id={city_id}&appid={KEY}")
    weather_obj = make_request(req, CODE)

    return get_readable_weather(weather_obj)


def get_by_zip_code(params: tuple) -> MessageInfo:
    CODE                   = 0
    zip_code, country_code = params
    req                    = urljoin(URL, f"weather?zip={zip_code},{country_code}&appid={KEY}")
    weather_obj            = make_request(req, CODE)

    return get_readable_weather(weather_obj)


def get_by_multiple_geographic_coordinates(params: tuple) -> MessageInfo:
    CODE                                           = 1
    lon_left, lat_bottom, lon_right, lat_top, zoom = params
    req                                            = urljoin(URL, f"box/city?bbox={lon_left},{lat_bottom},{lon_right},{lat_top},{zoom}&appid={KEY}")
    weather_obj                                    = make_request(req, CODE)
    return weather_obj


def get_by_cities_in_circle(params: tuple) -> List[MessageInfo]:
    CODE          = 2
    lat, lon, cnt = params
    req           = urljoin(URL, f"find?lat={lat}&lon={lon}&cnt={cnt}&appid={KEY}")
    weather_obj   = make_request(req, CODE)

    return weather_obj


def get_by_ceveral_city_ids(params: tuple) -> MessageInfo:
    CODE = 3
    city_ids = ','.join([str(x) for x in params])
    req = urljoin(URL, f"group?id={city_ids}&units=metric&appid={KEY}")
    weather_obj = make_request(req, CODE)

    return weather_obj

    
if __name__ == "__main__":
    pass
