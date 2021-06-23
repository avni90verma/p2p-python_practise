class Employee:
    company = "Visa"

class Freelancer:
    company = "Fever"
    level = 2
    def upgrade_level(self):
        self.level = self.level+1

class Programmer(Employee,Freelancer):
    name = "rohit"


p = Programmer()
p.upgrade_level()
print(p.level)
print(p.company)

