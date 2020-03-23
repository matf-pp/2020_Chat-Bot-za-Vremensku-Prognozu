import json
from models.CompleteWeatherInfo import CompleteWeatherInfo

def parse_json(JSON):
    weather_info = CompleteWeatherInfo.parse_obj(JSON)
    return weather_info

if __name__ == "__main__":
    pass
