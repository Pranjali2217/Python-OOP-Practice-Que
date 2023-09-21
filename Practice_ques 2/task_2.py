class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        print("area of rectangle is: ",self.length*self.width)

    def perimeter(self):
        print("perimeter of rectangle is: ",self.length + self.width)

obj=rectangle(4,8)
obj.area()
obj.perimeter()

