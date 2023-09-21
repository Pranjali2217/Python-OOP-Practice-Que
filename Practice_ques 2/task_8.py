class Temperature:
    def __init__(self,celsius):
        self.celsius=celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self,temperature):
        self._celsius=temperature
        print("temperature in celsius is: ",self._celsius)

    def fahrenheit(self):
        Fahrenheit = self.celsius * 1.8 +32
        print("temperature in fahrenheit is: ",Fahrenheit)

obj= Temperature(32)
obj.celsius
obj.fahrenheit()