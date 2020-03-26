import json
from models.OneCityWeatherParser import CompleteWeatherInfo
from models.LatLonCitiesWeatherParser import CompleteWeatherInfo

def parse_1_json(JSON):
    weather_info = CompleteWeatherInfo.parse_obj(JSON)
    return weather_info

def parse_ll_json(JSON):
    weather_info = CompleteWeatherInfo.parse_obj(JSON)
    return weather_info


def parse_r_json(JSON):
    pass


if __name__ == "__main__":
    pass
