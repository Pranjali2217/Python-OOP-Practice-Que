class Parent1:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def method1(self):
        print('I am',self.name,self.age,'year old')

class Parent2(Parent1):
    def __init__(self,name,age,department):
        self.department=department
        Parent1.__init__(self,name,age)

    def method2(self):
        print('I am from',self.department,'department')

class Child(Parent2):
    def __init__(self,name,age,department,company_name):
        self.company_name=company_name
        Parent2.__init__(self,name,age,department)

    def method3(self):
        print("my company name is",self.company_name)

child=Child('Pranjali',22,'Computer','UST')
child.method1()
child.method2()
child.method3()