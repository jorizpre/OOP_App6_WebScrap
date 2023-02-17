from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from temperature import Temperature
from calory import Calory

app = Flask(__name__) # __name__ contains the string of the current folder path

# Definition of Pages in our App
class HomePage(MethodView):
    def get(self):
        return render_template("index.html") # By convention Flask knows it should look for the HTML file in the "templates" folder

class CaloriesFormPage(MethodView):
    
    def get(self):
        calories_form = CaloriesForm()
        return render_template("calories_form_page.html", 
                               caloriesform=calories_form)
    
    def post(self):
        calories_form = CaloriesForm(request.form)
        
        # Coming from the WebApp Form:
        weight = float(calories_form.weight.data)
        height = float(calories_form.height.data)
        age= float(calories_form.age.data)

        city = calories_form.city.data
        country= calories_form.country.data
        
        # Coming from the Backend Calc tool using the form Inputs:
        temperature = Temperature(country = country, city = city).get()
        calories = str(Calory(weight= weight, height = height, age = age, temperature = temperature).calculate())

        return render_template("calories_form_page.html",
                               caloriesform=calories_form,
                               calories = calories,
                               result=True)



class CaloriesForm(Form):
    weight = StringField("Fill your weight: ", default="85")
    height = StringField("Fill your height: ", default= "185")
    age = StringField("Fill your age: ", default= "29")
    city = StringField("Fill your city: ", default= "Copenhagen")
    country = StringField("Fill your country: ", default= "Denmark")

    button = SubmitField("Calculate")


# Creating URL for our App pages
app.add_url_rule('/', view_func= HomePage.as_view('home_page'))
app.add_url_rule('/calories_form', view_func= CaloriesFormPage.as_view('calories_form_page'))


app.run(debug=True) # debug allows us to not have to stop and run the app every time we make changes 