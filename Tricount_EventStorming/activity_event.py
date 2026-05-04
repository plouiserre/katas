from dataclasses import dataclass

@dataclass(frozen=True)
class ActivityEvent : 
    name : str
    paymaster : str
    participants : tuple[str, ...]
    price: float 
    