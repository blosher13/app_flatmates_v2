from flask.views import MethodView
from flask import Flask, render_template, request
from wtforms import Form, StringField, SubmitField
from flatmates_bill import flat

app = Flask(__name__) #instantiate flask class

class HomePage(MethodView):
    def __init__(self):
        pass
    def get(self):
        return render_template('index.html')

class BillFormPage(MethodView):
    def __init__(self):
        pass
    def get(self):
        bill_form = BillForm()
        return render_template('billpage.html',billform=bill_form)

class ResultsPage(MethodView):
    def post(self):
        bill_form = BillForm(request.form)
        amount = int(bill_form.amount.data) #data is a property of the form widget
        period = bill_form.period.data

        f1_name = bill_form.f1_name.data
        f1_days = int(bill_form.f1_days.data)
        f2_name = bill_form.f2_name.data
        f2_days = int(bill_form.f2_days.data)

        the_bill = flat.Bill(amount, period).bill()
        f1 = flat.Flatmate(f1_name, f1_days)
        f1_pay = flat.Flatmate(f1_name, f1_days).pays(the_bill, f2_days)
        f2_pay = flat.Flatmate(f2_name, f2_days).pays(the_bill, f1_days)  
        f2 = flat.Flatmate(f2_name, f2_days)
        return render_template('resultspage.html',the_bill=the_bill, f1=f1, f1_pay=f1_pay, f2_pay=f2_pay, f2=f2)

class BillForm(Form):

    amount = StringField("Bill Amount: ")
    period = StringField("Bill Period: ")
    f1_name = StringField("FlatMate1 Name: ")
    f1_days = StringField("FlatMate1 Days: ")
    f2_name = StringField("FlatMate2 Name: ")
    f2_days = StringField("FlatMate2 Days: ")
    submit_button = SubmitField('Calculate')

app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_page'))
app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))

app.run(debug=True)