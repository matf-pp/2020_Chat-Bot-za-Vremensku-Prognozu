import utils
from input_parser import (
    is_exit_command,
    determine_response,
)

from models.OneCityWeather import CompleteWeatherInfo
from models.MessageInfo import MessageInfo
from models.ChatbotResponse import ChatbotResponse, ClientError, ServerError, HelpString
from typing import Tuple, Union, List
from backend import set_key_and_url

class ChatHandler:

    def __init__(self):
        self.chatbot = 'ChatBot'
        self.username = 'User'

    def assign_message_info(self, user: str) -> str:
        return f'[{user} @ {utils.get_current_time()}]: '

    def display_welcome_message(self) -> str:
        chat_response = f'{self.assign_message_info(self.chatbot)} Ask me a question about the weather, \nor type "help" if you are not sure what to do!\n'
        return chat_response
    
    def missing_info_handler(self) -> str:
        chat_response = f'\n{self.assign_message_info(self.chatbot)} .env file is missing or incomplete.\nPlease provide the application with your API KEY and URL in order to make\nrequests. Enter them in format: KEY: your_key, URL: your_url.\n\nCorrect formats are:\nAPI KEY: english alphabet letters and numbers\nURL: needs to start with: http://api.openweathermap.org/data/ and then API version should be added.\nFor more info, check help.\n'
        return chat_response
    
    def wrong_api_key_or_url_format(self) -> str:
        chat_response = f'\n{self.assign_message_info(self.chatbot)} API KEY or URL in wrong format.\nCorrect formats are:\nAPI KEY: english alphabet letters and numbers\nURL: needs to start with: http://api.openweathermap.org/data/ and then API version should be added.\nFor more info, check help.\n'
        return chat_response

    def get_chatbot_response_for_single_city(self, response: MessageInfo) -> str:
        chat_response = f'{self.assign_message_info(self.chatbot)}Current weather stats are:\n{response.convert_info_to_chat_format()}\n'
        return chat_response

    def get_chatbot_response_for_tuple(self, response:Tuple):
        set_key_and_url(response)
        chat_response = f'{self.assign_message_info(self.chatbot)} API KEY and URL successfully updated!\n'
        return chat_response

    def get_chatbot_response_for_multiple_cities(self, response: List[MessageInfo]) -> str:
        chat_response = f'{self.assign_message_info(self.chatbot)}Current weather stats are:\n'
        cities_info = ''
        
        for single_city_info in response:
            cities_info += single_city_info.convert_info_to_chat_format() + '\n'

        chat_response += cities_info
        return chat_response

    def get_wrong_user_input_response(self, error_msg: str) -> str:
        chat_response = f'{self.assign_message_info(self.chatbot)}{error_msg}\n\n'
        return chat_response

    def get_user_response(self, user_msg: str) -> str:
        chat_response = f'{self.assign_message_info(self.username)}{user_msg}\n\n'
        return chat_response

    def get_help_response(self) -> str:
        chat_response = (f"""
        To get weather by city name you can type something like 'London weather' or 'What's the weather in London'.
        To get weather by geografic coordinates you must specify lat and lon coordinates of a desired city (ordering is not important).
        To get weather around some area you must specify lat and lon coordinates and you must add something like: 'Get me weather around lat: X lon Y' of 'All cities near lat: X lon: Y.
        """)
        weather_by_city_name = "To get weather by city name you can type something like 'London weather' or 'What's the weather in London'."
        weather_by_coords = "To get weather by geografic coordinates you must specify lat and lon coordinates of a desired city (ordering is not important)."
        weather_by_circle = "To get weather around some area you must specify lat and lon coordinates and you must add something like: 'Get me weather around lat: X lon Y' or 'All cities near lat: X lon: Y."
        change_API_KEY_and_URL = "To change your API KEY and URL, you can type something like 'change KEY:your_key and URL:your_url'"
        set_API_KEY_and_URL = """Before application can make requests, you should make sure that .env file\nexists, with correct API key and URL in it. If you don't have .env file\nthe application will ask you to set API KEY and URL inside the GUI.\nIf you don't have API KEY, you should \nregister at: https://openweathermap.org/api and you'll get the key.
        """
        chat_response = f'{self.assign_message_info(self.chatbot)}\n{set_API_KEY_and_URL}\n{weather_by_city_name}\n\n{weather_by_coords}\n\n{weather_by_circle}\n\n{change_API_KEY_and_URL}\n\n'
        return chat_response

    def determine_chatbot_response(self, response: ChatbotResponse) -> str:
        if response is None:
            return self.get_wrong_user_input_response(ClientError)
        
        if response == ServerError:
            return self.get_wrong_user_input_response(ServerError)
        
        if response == ClientError:
            return self.get_wrong_user_input_response(ClientError)

        if response == HelpString:
            return self.get_help_response()
        
        if type(response) is MessageInfo:
            return self.get_chatbot_response_for_single_city(response)

        if type(response) is list:
            return self.get_chatbot_response_for_multiple_cities(response)
        
        if type(response) is tuple:
            return self.get_chatbot_response_for_tuple(response)
    
    def determine_user_response(self, user_msg: str) -> str:
        return self.get_user_response(user_msg)

    def handle_response(self, response: ChatbotResponse, user_msg: str) -> Tuple[str, str]:
        chatbot_response = self.determine_chatbot_response(response)
        user_response = self.determine_user_response(user_msg)

        return user_response, chatbot_response, 

    
def display_welcome_message():
    return ChatHandler().display_welcome_message()

def receive_message_and_make_response(user_msg: str) -> Tuple[str, str]:
    response = determine_response(user_msg)
    return ChatHandler().handle_response(response, user_msg)

def missing_info_handler():
    return ChatHandler().missing_info_handler()

def wrong_api_key_or_url_format():
    return ChatHandler().wrong_api_key_or_url_format()

if __name__ == "__main__":
    pass

