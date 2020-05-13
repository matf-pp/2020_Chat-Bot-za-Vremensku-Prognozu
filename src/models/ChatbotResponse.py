from typing import Union, List
from models.MessageInfo import MessageInfo


HelpString = 'help'
ServerError = 'There has been an error on our side, please try again later.'
ClientError = 'Your input is not recognized, please try again.'

ChatbotResponse = Union[MessageInfo, List[MessageInfo], str, None]