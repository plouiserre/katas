class Taeg : 
    def __init__(self, years, application_fee, monthly_payment, cost_guarantee, capital):
        self.years = years
        self.application_fee = application_fee 
        self.monthly_payment = monthly_payment 
        self.cost_guarantee = cost_guarantee
        self.capital = capital
        self.number_months = 0
        self.montly_paiment_all_included = 0

    def calculate(self):
        self.number_months = self.years *12
        application_fee_by_months = self.application_fee / self.number_months
        self.montly_paiment_all_included = self.monthly_payment + self.cost_guarantee + application_fee_by_months
        r_max = self.__iterate_to_find_r_max()
        r_min = round(r_max - 0.0001, 4)    
        r_min_r = self.__calcute_r(r_min)
        r_max_r = self.__calcute_r(r_max)
        TAEG =  round((r_min + (r_max - r_min) * r_min_r / (r_min_r - r_max_r)) *12*100, 2)
        return TAEG
    
    def __iterate_to_find_r_max(self) : 
        r = 0
        r_max = 0.0001
        while (r <= 0 ) :
            r = self.__calcute_r(r_max)
            if r <= 0 :
                r_max = round(r_max + 0.0001, 4)
        return r_max
    
    def __calcute_r(self, r_candidate):
        return self.capital - self.montly_paiment_all_included * (1 - (1+r_candidate)**-self.number_months)/r_candidate
    
