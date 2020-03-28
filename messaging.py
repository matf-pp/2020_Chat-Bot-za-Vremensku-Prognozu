import utils
from input_parser import (
    is_exit_command,
    determine_response,
)

from models.OneCityWeather import CompleteWeatherInfo
from models.MessageInfo import MessageInfo
from typing import Tuple, Union, List

class ChatHandler:

    def __init__(self):
        self.chatbot = 'ChatBot'
        self.username = 'User'

    def assign_message_info(self, user: str) -> str:
        return f'[{user} @ {utils.get_current_time()}]: '

    def get_chatbot_response_for_single_city(self, response: MessageInfo) -> str:
        chat_response = f'{self.assign_message_info(self.chatbot)}Current weather stats are:\n{response.convert_info_to_chat_format()}\n'
        return chat_response

    def get_chatbot_response_for_multiple_cities(self, response: List[MessageInfo]) -> str:
        chat_response = f'{self.assign_message_info(self.chatbot)}Current weather stats are:\n'
        cities_info = ''
        
        for single_city_info in response:
            cities_info += single_city_info.convert_info_to_chat_format() + '\n'

        chat_response += cities_info
        return chat_response

    def get_wrong_user_input_response(self) -> str:
        input_not_recognized_msg = 'Your input is not recognized, please try again.'
        chat_response = f'{self.assign_message_info(self.chatbot)}{input_not_recognized_msg}\n\n'
        return chat_response

    def get_user_response(self, user_msg: str) -> str:
        chat_response = f'{self.assign_message_info(self.username)}{user_msg}\n\n'
        return chat_response

    def determine_chatbot_response(self, response: Union[MessageInfo, List[MessageInfo], None]) -> str:
        if response is None:
            return self.get_wrong_user_input_response()
        
        elif type(response) is MessageInfo:
            return self.get_chatbot_response_for_single_city(response)
        else:
            #? Need handling for List[MessageInfo]
            return self.get_chatbot_response_for_multiple_cities(response)
    
    def determine_user_response(self, user_msg: str) -> str:
        return self.get_user_response(user_msg)


    def handle_response(self, response: Union[MessageInfo, List[MessageInfo], None], user_msg: str) -> Tuple[str, str]:
        chatbot_response = self.determine_chatbot_response(response)
        user_response = self.determine_user_response(user_msg)

        return user_response, chatbot_response, 

def receive_message_and_make_response(user_msg: str) -> Tuple[str, str]:
    response = determine_response(user_msg)
    return ChatHandler().handle_response(response, user_msg)


if __name__ == "__main__":
    user_response, chatbot_response = receive_message_and_make_response('London weather')
    print(user_response)
    print(chatbot_response)
