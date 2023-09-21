class temperature:
    def __init__(self,celsius):
        self.celsius=celsius

    @property
    def calculate(self):
        Fahrenheit=(self.celsius * 1.8) + 32
        print("temperature in fahrenheit is",Fahrenheit)

obj=temperature(32)
obj.calculate