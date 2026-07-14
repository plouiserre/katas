class Contact : 
    def __init__(self, first_name, last_name, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday

    def __eq__(self, other):
        return self.first_name == other.first_name and self.last_name == other.last_name and self.birthday == other.birthday