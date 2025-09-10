import calendar
import datetime


class Bill():
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period
    
    def bill(self):

        bill = self.amount
        return bill

class Flatmate():
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, days_in_house_f2):

        amount_to_pay = round(bill * (self.days_in_house/ (self.days_in_house + days_in_house_f2)), 2)
        return f'{self.name} pays: ${amount_to_pay}'

