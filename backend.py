from urllib.parse import urljoin
import requests
import os
from dotenv import load_dotenv
from models.MessageInfo import MessageInfo
from models.CombinedInfo import CombinedInfo
from models import (CityInCircleWeather, ManyCitiesWeather, OneCityWeather)
from scaling_and_conversion import readable_weather
from typing import Union, List, Tuple

load_dotenv()

KEY = os.getenv("KEY")
URL = os.getenv("URL")


def make_request(req: str) -> CombinedInfo:
    res = requests.get(req)

    return res


def get_readable_weather(complete_weather_object: CombinedInfo) -> Union[MessageInfo, List[MessageInfo]]:
    if isinstance(complete_weather_object, OneCityWeather.CompleteWeatherInfo):
        readable_object = readable_weather(complete_weather_object)
        
        return readable_object
    
    else:
        readable_object_list = []
        for obj in complete_weather_object.list:
            readable_object = readable_weather(obj)
            readable_object_list.append(readable_object)

        return readable_object_list


def get_by_city_name(params: str) -> MessageInfo:
    city_name   = params
    req         = urljoin(URL, f"weather?q={city_name}&appid={KEY}")    
    print(req)
    obj         = make_request(req)
    weather_obj = OneCityWeather.CompleteWeatherInfo.parse_obj(obj.json())

    return get_readable_weather(weather_obj)


def get_by_geographic_coordinates(params: Tuple[str, str]) -> MessageInfo:
    print('get_by_geographic_coordinates')
    lat, lon    = params
    req         = urljoin(URL, f"weather?lat={lat}&lon={lon}&appid={KEY}")
    obj         = make_request(req)
    weather_obj = OneCityWeather.CompleteWeatherInfo.parse_obj(obj.json())
    
    return get_readable_weather(weather_obj)


def get_by_city_id(params: int) -> MessageInfo:
    city_id     = params
    req         = urljoin(URL, f"weather?id={city_id}&appid={KEY}")
    obj         = make_request(req)
    weather_obj = OneCityWeather.CompleteWeatherInfo.parse_obj(obj.json())

    return get_readable_weather(weather_obj)


def get_by_zip_code(params: tuple) -> MessageInfo:
    zip_code, country_code = params
    req                    = urljoin(URL, f"weather?zip={zip_code},{country_code}&appid={KEY}")
    weather_obj            = make_request(req)
    obj         = make_request(req)
    weather_obj = OneCityWeather.CompleteWeatherInfo.parse_obj(obj.json())
    
    return get_readable_weather(weather_obj)


def get_by_cities_in_circle(params: Tuple[str, str]) -> List[MessageInfo]:
    print('get_by_cities_in_circle')
    default_count = 20
    lat, lon = params
    req           = urljoin(URL, f"find?lat={lat}&lon={lon}&cnt={default_count}&appid={KEY}")
    print(req)
    weather_obj   = make_request(req)
    obj         = make_request(req)

    weather_obj = CityInCircleWeather.CompleteWeatherInfo.parse_obj(obj.json())
    return get_readable_weather(weather_obj)


def get_by_ceveral_city_ids(params: tuple) -> MessageInfo:
    city_ids = ','.join([str(x) for x in params])
    req = urljoin(URL, f"group?id={city_ids}&units=metric&appid={KEY}")
    print(req)
    weather_obj   = make_request(req)
    obj         = make_request(req)
    weather_obj = ManyCitiesWeather.CompleteWeatherInfo.parse_obj(obj.json())

    return get_readable_weather(weather_obj)

    
if __name__ == "__main__":
    pass