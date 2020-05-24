import re
from urllib.parse import urljoin

from backend import (
    get_by_geographic_coordinates,
    get_by_city_name,
    get_by_cities_in_circle,
    make_request
)
from models.OneCityWeather import CompleteWeatherInfo
from typing import Union, Tuple, List, Optional
from models.MessageInfo import MessageInfo
from models.ChatbotResponse import ChatbotResponse, HelpString


REGEX_FLAGS = re.I | re.S

def is_exit_command(user_input: str) -> bool:
    return user_input.lower().strip() == 'exit'

def contains_city_name(user_input: str) -> Optional[str]:
    """
    Receives user_input 

    Returns city_name or None if the city name is not found
    """

    regex = re.compile(r'.*weather.*in\s+(?P<city_name>[a-z]+).*', REGEX_FLAGS)
    match = regex.match(user_input)    
    if match:
        return match.group('city_name')

    regex = re.compile(r'(.* |^)(?P<city_name>[a-z]+)\s+weather.*', REGEX_FLAGS)
    match = regex.match(user_input)    
    if match:
        return match.group('city_name')
    
    return None

def contains_lat_lon(user_input: str) -> Optional[Tuple[str, str]]:
    regex = re.compile(r'.*(lat:|lat)\s*(?P<lat>[0-9]{1,3}(\.[0-9]+){0,1}).* (lon:|lon)\s*(?P<lon>[0-9]{1,3}(\.[0-9]+){0,1}).*', REGEX_FLAGS)
    match = regex.match(user_input)    
    if match:
        return (match.group('lat'), match.group('lon'))

    regex = re.compile(r'.*(lon:|lon)\s*(?P<lon>[0-9]{1,3}(\.[0-9]+){0,1}).* (lat:|lat)\s*(?P<lat>[0-9]{1,3}(\.[0-9]+){0,1}).*', REGEX_FLAGS)
    match = regex.match(user_input)    
    if match:
        return (match.group('lat'), match.group('lon'))

    return None

def contains_circle(user_input: str) -> Optional[Tuple[str, str]]:
    lat_lon_base = r'.*(lat:|lat)\s*(?P<lat>[0-9]{1,3}(\.[0-9]+){0,1}).* (lon:|lon)\s*(?P<lon>[0-9]{1,3}(\.[0-9]+){0,1}).*'
    lon_lat_base = r'.*(lon:|lon)\s*(?P<lon>[0-9]{1,3}(\.[0-9]+){0,1}).* (lat:|lat)\s*(?P<lat>[0-9]{1,3}(\.[0-9]+){0,1}).*'
    

    circle_around_base = r'(in\s+circle)?\s+around'
    regex = re.compile(circle_around_base + lat_lon_base, REGEX_FLAGS)
    match = regex.match(user_input)    
    if match:
        return (match.group('lat'), match.group('lon'))

    regex = re.compile(circle_around_base + lon_lat_base, REGEX_FLAGS)
    match = regex.match(user_input)    
    if match:
        return (match.group('lat'), match.group('lon'))

    all_cities_around_base = r'all\s+cities\s+(around|in\s+the\s+proximity\s+(of){0,1}|near(by){0,1}).*'
    regex = re.compile(all_cities_around_base + lat_lon_base, REGEX_FLAGS)
    match = regex.match(user_input)    
    if match:
        return (match.group('lat'), match.group('lon'))

    regex = re.compile(all_cities_around_base + lon_lat_base, REGEX_FLAGS)
    match = regex.match(user_input)    
    if match:
        return (match.group('lat'), match.group('lon'))

def contains_API_KEY_and_URL(user_input) -> Optional[Tuple[str, str]]:
    api_url_base = r".*(KEY)\s*:\s*(?P<api_key>[A-Za-z0-9]+).* (URL|url)\s*:\s*(?P<url>http:\/\/api.openweathermap.org\/data\/[2-9]\.[0-9]\/.*)"
    url_api_base = r".*(URL)\s*:\s*(?P<url>http:\/\/api.openweathermap.org\/data\/[2-9]\.[0-9]\/.* (KEY|key)\s*:\s*(?P<api_key>[A-Za-z0-9]+).*)"

    regex = re.compile(api_url_base, REGEX_FLAGS)
    match = regex.match(user_input)

    if match:
        return (match.group('api_key'), match.group('url'))

    regex = re.compile(url_api_base, REGEX_FLAGS)
    match = regex.match(user_input)
    if match:
        return (match.group('api_key'), match.group('url'))

    return None  

def contains_valid_api_key_and_url(user_input: str) -> Optional[Tuple[str, str]]:
    key_and_url = contains_API_KEY_and_URL(user_input) 
    if not key_and_url:
        return None

    key, url = key_and_url
    #? Just check if we'll get 4** response, if that's the case, something is wrong with key and/or url
    req = urljoin(url, f"weather?q=Belgrade&appid={key}") 

    res = make_request(req)

    if res.status_code // 100 == 4:
        return None
    
    return key, url


def contains_help(user_input: str) -> Optional[str]:
    regex = re.compile(r'help', REGEX_FLAGS)
    match = regex.match(user_input)    
    if match:
        return HelpString

def user_making_request(user_input: str):
    return (contains_circle(user_input) or contains_lat_lon(user_input) or contains_city_name(user_input))

def determine_response(user_input: str) -> ChatbotResponse:
    params = contains_circle(user_input)
    if params:
        return get_by_cities_in_circle(params)
    
    params = contains_lat_lon(user_input)
    if params:
        return get_by_geographic_coordinates(params)

    params = contains_city_name(user_input)
    if params:
        return get_by_city_name(params)

    params = contains_help(user_input)
    if params:
        return HelpString

    key_and_url = contains_valid_api_key_and_url(user_input)
    if key_and_url:
        return key_and_url    

    return None

if __name__ == "__main__":
    pass
