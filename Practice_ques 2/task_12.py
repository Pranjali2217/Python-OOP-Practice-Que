class Employee:
    all_salaries=[]

    def __init__(self,employee_name,employee_salary):
        self.employee_name = employee_name 
        self.employee_salary= employee_salary
        Employee.all_salaries.append(employee_salary)

    @classmethod
    def calculate_avg_salary(cls):
            total_salary = sum(cls.all_salaries)
            average_salary = total_salary / len(cls.all_salaries)
            return average_salary
 
employee1 = Employee("Alice", 50000)
employee2 = Employee("Bob", 60000)
employee3 = Employee("Charlie", 70000)

average_salary = Employee.calculate_avg_salary()

print("average salary of all the employees is: ",average_salary)



