from dataclasses import dataclass

@dataclass(frozen=True)
class Activity : 
    name : str
    participants : tuple[str, ...]
    price: float 
    