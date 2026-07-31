from dataclasses import dataclass

@dataclass(frozen=True)
class PostRequest : 
    author_name : str 
    message : str