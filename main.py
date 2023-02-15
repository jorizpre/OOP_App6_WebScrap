from calory import Calory
from temperature import Temperature

w = float(input("Enter your weight: "))
h = float(input("Enter your height: "))
a = float(input("Enter your age: "))
country = str(input("Enter your country: "))
city = str(input ("Enter your city: "))

t = Temperature(country=country, city=city).get()
calories = Calory(w,h,a,t).calculate()

print("Your consumed calories are " + str(calories))