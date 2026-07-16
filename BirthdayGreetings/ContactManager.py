from abc import ABC, abstractmethod
from typing import Iterator

from BirthdayGreetings.Contact import Contact

class ContactManager(ABC):
    @abstractmethod
    def get_all_contacts() -> Iterator[Contact] : 
        pass