class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("name of person is: ",self.name)
        print("age of person is: ",self.age)

obj=person('harry',22)
obj.display()
obj1=person('pranjali',23)
obj1.display()