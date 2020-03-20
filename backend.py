from urllib.parse import urljoin
import requests
import os
from dotenv import load_dotenv
from json_parser import parse_json

load_dotenv()

KEY = os.getenv("KEY")
URL = os.getenv("URL")

KELVIN_TO_DEGREES_CONST = 273.15
PRECISION = 2

def kelvins_to_degrees(obj):
    obj.main.temp       = round(obj.main.temp - KELVIN_TO_DEGREES_CONST, PRECISION)
    obj.main.feels_like = round(obj.main.feels_like - KELVIN_TO_DEGREES_CONST, PRECISION)
    obj.main.temp_min   = round(obj.main.temp_min - KELVIN_TO_DEGREES_CONST, PRECISION)
    obj.main.temp_max   = round(obj.main.temp_max - KELVIN_TO_DEGREES_CONST, PRECISION)

    return obj

def get_by_city_name(params):
    city_name = params
    req = urljoin(URL, f"?q={city_name}&appid={KEY}")
    res = requests.get(req)
    weather_obj = parse_json(res.json())
    weather_obj_scaled = kelvins_to_degrees(weather_obj)
    return weather_obj_scaled
   
def get_by_lat_lon(params):
    lat, lon = params
    req = urljoin(URL, f"?lat={lat}&lon={lon}&appid={KEY}")
    res = requests.get(req)
    weather_obj = parse_json(res.json())
    weather_obj_scaled = kelvins_to_degrees(weather_obj)
    return weather_obj_scaled
    
if __name__ == "__main__":
    pass
