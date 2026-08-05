import datetime
from abc import ABC, abstractmethod

class Clock(ABC): 

    @abstractmethod
    def now()->datetime :
        pass