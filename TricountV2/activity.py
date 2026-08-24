class Activity :
    def __init__(self, name, price, participants_name, payer):
        self.name = name
        self.price = price
        self.participants_name = participants_name
        self.payer = payer

    @staticmethod
    def create(name, price, participants_name, payer):
        return Activity(name, price, participants_name, payer)