class Calory:
    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature
    
    def calculate(self):
        return 10*self.weight + 6.25*self.height - 5*self.age + 5 - 10*self.temperature

# my_calories = Calory(85,185,29,20).calculate()
# print(my_calories)