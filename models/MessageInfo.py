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
        self.name : Union[str, None] = None  

    def convert_info_to_chat_format(self) -> str:
        chat_format_str = ''
        chat_format_str += self.add_to_chat_if_exists(self.name, "Name: ")
        chat_format_str += self.add_to_chat_if_exists(self.temp, 'Current temp:')
        chat_format_str += self.add_to_chat_if_exists(self.feels_like, 'Feels like:')
        chat_format_str += self.add_to_chat_if_exists(self.temp_min, 'Min temp:')
        chat_format_str += self.add_to_chat_if_exists(self.temp_max, 'Max temp:')
        chat_format_str += self.add_to_chat_if_exists(self.pressure, 'Pressure:')
        chat_format_str += self.add_to_chat_if_exists(self.humidity, 'Humidity:')
        chat_format_str += self.add_to_chat_if_exists(self.wind_speed, 'Wind speed:')
        
        return chat_format_str

    def add_to_chat_if_exists(self, prop: Union[str, None], msg: str) -> str:
        if prop is None:
            return ''
        
        return f'\t{msg} {prop}\n'


if __name__ == "__main__":
    pass