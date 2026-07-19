from dataclasses import dataclass

@dataclass(frozen=True)
class Template : 
    message : str
    code_to_replace : str