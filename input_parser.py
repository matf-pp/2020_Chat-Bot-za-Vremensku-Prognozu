import re

from backend import (
    get_by_geographic_coordinates,
    get_by_city_name,
    get_by_cities_in_circle,
)
from models.OneCityWeather import CompleteWeatherInfo
from typing import Union, Tuple, List
from models.MessageInfo import MessageInfo
from models.ChatbotResponse import ChatbotResponse, HelpString

REGEX_FLAGS = re.I | re.S

def is_exit_command(user_input: str) -> bool:
    return user_input.lower().strip() == 'exit'

def contains_city_name(user_input: str) -> Union[str, None]:
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

def contains_lat_lon(user_input: str) -> Union[Tuple[str, str], None]:
    regex = re.compile(r'.*(lat:|lat)\s*(?P<lat>[0-9]{1,3}(\.[0-9]+){0,1}).* (lon:|lon)\s*(?P<lon>[0-9]{1,3}(\.[0-9]+){0,1}).*', REGEX_FLAGS)
    match = regex.match(user_input)    
    if match:
        return (match.group('lat'), match.group('lon'))

    regex = re.compile(r'.*(lon:|lon)\s*(?P<lon>[0-9]{1,3}(\.[0-9]+){0,1}).* (lat:|lat)\s*(?P<lat>[0-9]{1,3}(\.[0-9]+){0,1}).*', REGEX_FLAGS)
    match = regex.match(user_input)    
    if match:
        return (match.group('lat'), match.group('lon'))

    return None

def contains_circle(user_input: str) -> Union[Tuple[str, str]]:
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
    
def contains_help(user_input: str) -> str:
    regex = re.compile(r'help', REGEX_FLAGS)
    match = regex.match(user_input)    
    if match:
        return HelpString

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

    return None

if __name__ == "__main__":
    pass
