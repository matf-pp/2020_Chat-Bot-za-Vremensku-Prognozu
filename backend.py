from urllib.parse import urljoin
import requests
import os
from dotenv import load_dotenv
from json_parser import (CompleteWeatherInfo, parse_json)

load_dotenv()

KEY = os.getenv("KEY")
URL = os.getenv("URL")


def scale_temperature(temp):   
    
    return round(temp - 273.15, 2)


def kelvins_to_degrees(obj:CompleteWeatherInfo):
    obj.main.temp       = scale_temperature(obj.main.temp)
    obj.main.feels_like = scale_temperature(obj.main.feels_like)
    obj.main.temp_min   = scale_temperature(obj.main.temp_min)
    obj.main.temp_max   = scale_temperature(obj.main.temp_max)

    return obj


def make_request(req):
    res                = requests.get(req)
    weather_obj        = parse_json(res.json())
    
    return weather_obj


def get_by_city_name(params) -> CompleteWeatherInfo:
    city_name = params
    req       = urljoin(URL, f"?q={city_name}&appid={KEY}")    
    weather_obj = make_request(req)
    
    return kelvins_to_degrees(weather_obj)
   

def get_by_lat_lon(params) -> CompleteWeatherInfo:
    lat, lon = params
    req      = urljoin(URL, f"?lat={lat}&lon={lon}&appid={KEY}")
    weather_obj = make_request(req)
    
    return kelvins_to_degrees(weather_obj)
    
    
if __name__ == "__main__":
    pass
