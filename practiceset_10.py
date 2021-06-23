# class programmer:
#     company = "Microsoft"
#     def __init__(self,name,product):
#         self.name = name
#         self.product = product
#     def getinfo(self):
#         print(f"The name of programmer is {self.name}")
#         print(f"The product is {self.product}")

# Avni = programmer("Avni","Youtube")
# Sita = programmer("Sita", "Google")

# Avni.getinfo()



class calculator:
    def __init__(self,num):
        self.num = num

    @staticmethod
    def greet():
        print("Hello")    

    def square(self):
        print(f"the square of {self.num} is {self.num**2}")

    def cube(self):
        print(f"the square of {self.num} is {self.num**3}")
    
    def squareroot(self):
        print(f"the square of {self.num} is {self.num**0.5}")

Avni = calculator(26) 
Avni.greet()       
Avni.square()
Avni.cube()
Avni.squareroot()




class train:

    def __init__ (self, name, fare, seats):
        
        self.name = name
        self.fare = fare
        self.seats = seats

       
    def get_status(self):
        print(f"The name of train is{self.name} ")
        print(f"The seats of train is{self.seats} ")
        
    def fareinfo(self):
        print(f"The fair of train is{self.fare}")

Train = train("Rajdhani Express", 300 , 80)            
Train.get_status()
Train.fareinfo()


  
