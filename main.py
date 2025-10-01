from flask.views import MethodView
from flask import Flask, render_template

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
        return render_template('billpage.html')

class ResultsPage():
    def __init__(self):
        pass

class BillForm():
    def __init__(self):
        pass

app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill'))

app.run(debug=True)