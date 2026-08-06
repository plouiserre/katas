from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Author : 
    name : str
    following_persons : list[Author]