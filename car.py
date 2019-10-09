class Machine():
    def __init__(self, model, milage, typeofcar):
        self.model = model
        self.milage = milage
        self.type = typeofcar

    def price(self):
        return "The price is $200,000"

class Car(Machine):
    def __init__(self, model, milage, typeofcar, year, custom):
        super().__init__(model, milage, typeofcar)
        self.yearofmake = year
        self.customization = custom
