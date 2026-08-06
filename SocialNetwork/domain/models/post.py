import datetime
from SocialNetwork.domain.models.account import Account

from dataclasses import dataclass

@dataclass(frozen=True)
class Post : 
    account : Account
    content_message : str
    date_posting : datetime

    @staticmethod
    def create_post(account, content_message, date_posting): 
        return Post(account, content_message, date_posting)
