import re

from backend import (
    get_by_lat_lon,
    get_by_city_name
)

REGEX_FLAGS = re.I | re.S

def is_exit_command(user_input):
    return user_input.lower().strip() == 'exit'

def contains_city_name(user_input):
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

def contains_lat_lon(user_input):
    regex = re.compile(r'.*(lat:|lat)\s*(?P<lat>[0-9]{1,3}(\.[0-9]+){0,1}).* (lon:|lon)\s*(?P<lon>[0-9]{1,3}(\.[0-9]+){0,1}).*', REGEX_FLAGS)
    match = regex.match(user_input)    
    if match:
        return (match.group('lat'), match.group('lon'))

    return None

def determine_response(user_input):
    params = contains_lat_lon(user_input)
    if params:
        print(params)
        return get_by_lat_lon(params)

    params = contains_city_name(user_input)
    if params:
        print(params)
        return get_by_city_name(params)

    return None


if __name__ == "__main__":
    pass