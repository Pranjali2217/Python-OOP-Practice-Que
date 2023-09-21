class Student:
    total_students = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.total_students += 1

obj1 = Student('pranjali',22)
obj2 = Student('Akanksha',23)
print(obj1.name, obj1.age)
print(obj2.name, obj2.age)
print("total students are: ",Student.total_students)