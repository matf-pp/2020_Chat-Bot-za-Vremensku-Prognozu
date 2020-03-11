from backend import (
    get_by_lat_lon,
    get_by_city_name
)

def is_exit_command(user_input):
    return user_input.lower().strip() == 'exit'

def contains_city_name(user_input):
    return 'contains_city_name'

def contains_lat_lon(user_input):
    return 'contains_lat_lon'

def determine_response(user_input):
    params = contains_lat_lon(user_input)
    if params:
        return get_by_lat_lon(params)

    params = contains_city_name(user_input)
    if contains_city_name(user_input):
        return get_by_city_name(params)


if __name__ == "__main__":
    pass