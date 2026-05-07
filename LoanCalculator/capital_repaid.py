class Capital_Repaid: 
    def __init__(self, montly_payment, interests):
        self.montly_payment = montly_payment
        self.interests = interests

    def calculate_amount(self): 
        return round(self.montly_payment -  self.interests, 2)