from fpdf import FPDF

class ReportBuilder():
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
