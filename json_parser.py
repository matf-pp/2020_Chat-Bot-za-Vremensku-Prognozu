import json
from models.OneCityWeather      import CompleteWeatherInfo  
from models.CityInCircleWeather import CompleteWeatherInfo
from models.ManyCitiesWeather   import CompleteWeatherInfo


def parse_json(JSON)->CompleteWeatherInfo:
    weather_info = CompleteWeatherInfo.parse_obj(JSON)
    
    return weather_info

if __name__ == "__main__":
    pass
