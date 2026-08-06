from dataclasses import dataclass

@dataclass(frozen=True)
class PostRequest : 
    account_name : str 
    message : str