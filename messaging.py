from input_parser import (
    is_exit_command,
    determine_response,
)

from datetime import datetime
from models.OneCityWeatherParser import CompleteWeatherInfo1
from typing import Tuple

CHATBOT_NAME = 'ChatBot'
USER_NAME = 'User'

def get_current_time() -> str:
    datetime_obj = datetime.now()
    current_time = datetime_obj.strftime('%d-%b-%Y : %H:%M:%S')
    return current_time

def assign_message_info(user: str) -> str:
    return f'[{user} @ {get_current_time()}]: '

def convert_chatbot_response_to_chat_format(response: CompleteWeatherInfo1, is_user = False) -> str:
    wind_speed = response.wind.speed
    temp = response.main.temp
    humidity = response.main.humidity

    chat_response = ( 
    f"""{assign_message_info(CHATBOT_NAME)}
    \tWeather stats are:
    \tCurrent temperature: {temp}
    \tCurrent humidity: {humidity}
    \tCurrent wind speed: {wind_speed}
    \n""")
    return chat_response

def convert_wrong_user_input_to_chat_format() -> str:
    input_not_recognized_msg = 'Your input is not recognized, please try again.'
    chat_response = f'{assign_message_info(CHATBOT_NAME)}{input_not_recognized_msg}\n\n'
    return chat_response

def convert_user_msg_to_chat_format(user_msg: str) -> str:
    chat_response = f'{assign_message_info(USER_NAME)}{user_msg}\n\n'
    return chat_response

def receive_message_and_make_response(user_msg: str) -> Tuple[str, str]:
    
    response = determine_response(user_msg)

    #! neki_dict[(response_type)] = neka_funkcija

    if not response:
        chatbot_response = convert_wrong_user_input_to_chat_format()   
    else:
        chatbot_response = convert_chatbot_response_to_chat_format(response)
    
    user_response = convert_user_msg_to_chat_format(user_msg)

    return user_response, chatbot_response



def main():
    print('Ask me a question about the weather\n')

    while True:
        user_input = input()

        if is_exit_command(user_input):
            print('Program exiting...')
            break
        
        response = determine_response(user_input)
        
        if not response:
            print(convert_wrong_user_input_to_chat_format())
        
        else:
            print(convert_chatbot_response_to_chat_format(response))
        
        

if __name__ == "__main__":
    user_response, chatbot_response = receive_message_and_make_response('London weather')
    print(user_response)
    print(chatbot_response)
