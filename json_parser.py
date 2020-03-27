import json
from models.OneCityWeatherParser      import CompleteWeatherInfo1  
from models.LatLonCitiesWeatherParser import CompleteWeatherInfoLL
from models.CityInCircleWeatherParser import CompleteWeatherInfoR
from models.ManyCitiesWeatherParser   import CompleteWeatherInfoM


def parse_1_json(JSON)->CompleteWeatherInfo1:
    weather_info = CompleteWeatherInfo1.parse_obj(JSON)
    
    return weather_info


def parse_ll_json(JSON)->CompleteWeatherInfoLL:
    weather_info = CompleteWeatherInfoLL.parse_obj(JSON)
    
    return weather_info


def parse_r_json(JSON)->CompleteWeatherInfoR:
    weather_info = CompleteWeatherInfoR.parse_obj(JSON)
    
    return weather_info


def parse_m_json(JSON)->CompleteWeatherInfoM:
    weather_info = CompleteWeatherInfoM.parse_obj(JSON)

    return weather_info


if __name__ == "__main__":
    pass
