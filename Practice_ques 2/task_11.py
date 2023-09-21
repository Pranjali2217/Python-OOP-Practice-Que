class Employee:
    department = 'IT'

    def __init__(self,name,employee_id):
        self.name = name
        self.employee_id =employee_id

    def display(self):
        print('my name is',self.name ,'and employee_id is',self.employee_id )

    @classmethod
    def from_string(cls,s):
        name,age = s.split(',')
        return cls(name, int(age))
    
employee=Employee('pranjali',1)
employee.display()

s='gauri,2'
employee=Employee.from_string(s)
employee.display()