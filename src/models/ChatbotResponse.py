from typing import Union, List
from models.MessageInfo import MessageInfo


HelpString = 'help'
ServerError = 'There has been an error on our side, please try again later.'
ClientError = 'Your weather query input is not recognized, or you provided invalid API KEY or URL.'

ChatbotResponse = Union[MessageInfo, List[MessageInfo], str, None]