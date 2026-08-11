import datetime

from dataclasses import dataclass

@dataclass(frozen=True)
class Post : 
    account_name : str
    content_message : str
    date_posting : datetime

    @staticmethod
    def create_post(account_name, content_message, date_posting): 
        return Post(account_name, content_message, date_posting)
