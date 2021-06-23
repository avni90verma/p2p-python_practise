class Employee:
    company = "Bharat Gas"
    salary = 4000
    salary_bonus = 500
    
    @property
    def totalsalary(self):
        return self.salary + self.salary_bonus

e = Employee()
print(e.totalsalary())        