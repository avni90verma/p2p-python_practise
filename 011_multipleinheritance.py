class Person:
    def __init__(self):
        print("Initailizing person")
        
    country = "India"

    def take_breath(self):
        print("I am Breathing")

class Employee:
    company = "Honda"
    
    def __init__(self):
        super().__init__()
        print("Initailizing Employee")
        


    def get_salary(self):
        print(f"The salary is {self.get.salary}")

    def take_breath(self):
        print("I am an employ so i am luckily breathing")

class Programmer(Employee):
    company = "Fiver"
    
        

    def get_salary(self):
        super().take_breath()
        print("i am breathing++")
        print("no salary to programmers")
p = Person()
e = Employee()
pr = Programmer()     
print(pr.get_salary())




