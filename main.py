from flask.views import MethodView
from flask import Flask, render_template, request
from wtforms import Form, StringField, SubmitField

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
        amount = bill_form.amount.data #data is a property of the form widget
        return amount

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