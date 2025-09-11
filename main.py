from flat import Bill, Flatmate
from fpdf import FPDF



class PdfReport():
    def __init__(self, filename):
        self.filename = filename

    def generate_report(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        flatmate1_pay = str(flatmate1.pays(bill.bill(), flatmate2.days_in_house))
        flatmate2_pay = str(flatmate2.pays(bill.bill(), flatmate1.days_in_house))
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt= f'{flatmate1.name} & {flatmate2.name} Bill', border=1, align='C', ln=1)
        pdf.cell(w=0, h=40, txt=f'For period: {bill.period}', border=1, align='C', ln=1)
        pdf.cell(w=0, h=40, txt=f'{flatmate1_pay}', border=1, align='C', ln=1)
        pdf.cell(w=0, h=40, txt=f'{flatmate2_pay}', border=1, align='C', ln=1)
        pdf.output(self.filename)
    pass

while True:
    try:
        bill_amount = int(input('Hi user, please enter bill amount: '))
        bill_period = input('What is the bill period? ex. December 2020 ')
        name_f1 = input('What is your name?')
        days_stayed_f1 = int(input(f'How many days did {name_f1} stay in the house during this period? '))
        name_f2 = input('What is your flatmate\'s name? ')
        days_stayed_f2 = int(input(f'How many days did {name_f2} stay in the house during this period?'))

        bill_f1_amount = Bill(bill_amount, bill_period).bill()
        bill_f2_amount = Bill(bill_amount, bill_period).bill()
        amount_f1 = Flatmate(name_f1, days_stayed_f1).pays(bill_f1_amount, days_stayed_f2)
        amount_f2 = Flatmate(name_f2, days_stayed_f2).pays(bill_f2_amount, days_stayed_f1)
        print(amount_f1, amount_f2)

        flatmate1 = Flatmate(name_f1, days_stayed_f1)
        flatmate2 = Flatmate(name_f2, days_stayed_f2)
        bill = Bill(bill_amount, bill_period)
        report = PdfReport('flatmate_file1.pdf')
        report.generate_report(flatmate1, flatmate2, bill)
        break
    except ValueError as e:
        print(e)