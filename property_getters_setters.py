class Car:
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def model(self):
        return self._model 
    
    @model.setter
    def model(self, value):
        self._model = value

car1 = Car()
car1.name = "TOYOTA"
car1.model = "XX3C"

print(car1.name)
print(car1.model)



