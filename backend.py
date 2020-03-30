from urllib.parse import urljoin
import requests
import os
from dotenv import load_dotenv
from models.MessageInfo import MessageInfo
from models.CombinedInfo import CombinedInfo
from models.ChatbotResponse import ClientError, ServerError, ChatbotResponse
from models import (CityInCircleWeather, ManyCitiesWeather, OneCityWeather)
from scaling_and_conversion import readable_weather
from typing import Union, List, Tuple

load_dotenv()

KEY = os.getenv("KEY")
URL = os.getenv("URL")


def make_request(req: str) -> Union[CombinedInfo, None]:
    res = requests.get(req)
    
    return res


def get_readable_weather(complete_weather_object: CombinedInfo) -> ChatbotResponse:

    CODE = int(complete_weather_object.cod / 100)

    if CODE == 4:
        return ClientError
    if  CODE == 5:
        return ServerError

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
    obj         = make_request(req)
    weather_obj = OneCityWeather.CompleteWeatherInfo.parse_obj(obj.json())

    return get_readable_weather(weather_obj)


def get_by_geographic_coordinates(params: Tuple[str, str]) -> MessageInfo:
    lat, lon    = params
    req         = urljoin(URL, f"weather?lat={lat}&lon={lon}&appid={KEY}")
    obj         = make_request(req)
    
    weather_obj = OneCityWeather.CompleteWeatherInfo.parse_obj(obj.json())
    
    return get_readable_weather(weather_obj)


def get_by_cities_in_circle(params: Tuple[str, str]) -> List[MessageInfo]:
    default_count = 20
    lat, lon = params
    req           = urljoin(URL, f"find?lat={lat}&lon={lon}&cnt={default_count}&appid={KEY}")
    obj         = make_request(req)
    weather_obj = CityInCircleWeather.CompleteWeatherInfo.parse_obj(obj.json())
    
    return get_readable_weather(weather_obj)

if __name__ == "__main__":
    pass
