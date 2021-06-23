class Employee():
    company = "Google"
    
    def getdetails(self):
        print("This is an employee")
class Programmer(Employee):
    language = "python"

    def get_language(self):
        print(f"the language is {self.language} ")


ob = Employee()
p = Programmer()
ob.getdetails()
p.get_language()

        

