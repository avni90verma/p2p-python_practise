class Employee:
    company = "camel"
    salary = 100
    location = "Delhi"

    # def change_salary(self,sal):
    #     self.salary = sal
    @classmethod
    def change_salary(cls , sal):
        cls.salary = sal



e = Employee()
print(e.salary)
e.change_salary(455)
print(e.salary)
print(Employee.salary)        