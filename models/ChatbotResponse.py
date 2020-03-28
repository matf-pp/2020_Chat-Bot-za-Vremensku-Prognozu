from typing import Union, List
from models.MessageInfo import MessageInfo

ChatbotResponse = Union[MessageInfo, List[MessageInfo], str, None]