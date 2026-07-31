from dataclasses import dataclass

@dataclass(frozen=True)
class Message : 
    author_name : str
    content_message : str
