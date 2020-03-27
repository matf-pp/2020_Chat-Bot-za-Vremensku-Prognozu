from typing import Union

class MessageInfo:
    def __init__(self):
        self.temp: Union[str, None] = None       
        self.feels_like: Union[str, None] = None 
        self.temp_min: Union[str, None] = None   
        self.temp_max: Union[str, None] = None   
        self.pressure: Union[str, None] = None 
        self.humidity: Union[str, None] = None   
        self.wind_speed: Union[str, None] = None      