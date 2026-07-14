from dataclasses import dataclass

@dataclass(frozen=True)
class Contact : 
    first_name : str
    last_name : str
    birthday :str

    def __eq__(self, other):
        return self.first_name == other.first_name and self.last_name == other.last_name and self.birthday == other.birthday