#OOPcoding writing level 1:
class car:
    colour = "black"
    brand  = "toyota"
    model = "2026"

carinfo=car()
print(car.colour)
print(car.model)
car.colour= "red"
print(car.colour)
print(car.brand)

#OOPcoding writing level 2:

class car:
     brand= 'BMW'
     colour = "grey"
     model = '2026'
car1= car()
print(car1.brand)
print(car1.model)
car1.colour = "orange"
print(car1.colour)

car2 = car()
print(car.model)
print(car.brand)
car2.colour = "black"
print(car2.colour)

#OOP coding writing level 3:
class student:
    def __init__(self,name, age, rollno):
        self.name= name
        self.age = age
        self.rollno = rollno
student1= student("hira",18,24)
student2= student("warda",21,32) 
print(student1.rollno)
print(student2.name)
print(student1.name)
print(student2.age)

#OPP coding writing level 4:

class student:
    def __init__(self,name, age , grade):
        self.name = name
        self.age = age
        self.grade = grade
    def show(self):
        print("name =",self.name)
        print("age=", self.age)
        print("grade",self.grade)

student1= student("hira",19,"A")
student2= student("zara",20,"B")

student1.show()
student2.show()

#OOP coding writing level 5: 
class laptop:
    brand= "DELL"
    country = "USA"
    def __init__(self,ram,price,model):
        self.ram= ram
        self.price= price
        self.model = model
    def info(self):
        print("ram=",self.ram)
        print("price=",self.price)
        print("model=",self.model)
        print("brand =",laptop.brand)
        print("country=",laptop.country)
laptop1= laptop(234,500,2026)
laptop2= laptop(300,400,2020)
laptop1.info()
laptop2.info()

#OOPcoding writing level 6:

class pizza:
    def __init__(self,size= 10,topping= "cheese",price = 1200):
     #   self.size = size
      #  self.topping = topping
      #  self.price = price
     def func(self):
        print("the size of pizza:",self.size)
        print("the topping is:", self.topping)
        print("the price is:",self.price)
infopizza= pizza(8,"pepperoni",1500)
infopizza.func()
pizza2= pizza()
pizza2.func()


#OOP coding level 7:
class bank :
    def __init__(self,name,balance):
        self.name= name
        self.balance= balance
    def show__balance(self):
        print("name :",self.name)
        print("current balance :", self.balance)
customer1 = bank("Hira",25000)
customer2= bank("Warda",5000)
customer1.show__balance()
customer2.show__balance()

#OOP code writing level 8:

class vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def show__info(self):
        print("brand :",self.brand)
        print("model :", self.model)
class car(vehicle):
     def __init__(self, brand, model):
         super().__init__(brand, model)
info =  car("bmw",2026)
info.show__info()

#OOP code writing level 9:

class dog:
    def __init__(self,sound):
        self.sound = sound
    def dog__sound(self):
        print("The Dog sound:",self.sound)
class puppy(dog):
 def __init__(self, sound):
       # super().__init__(sound)
     def  dog__sound(self):
       print("the puppy sound:",self.sound)
puppy1= puppy("woof")
dog1= dog("barkk")
dog1.dog__sound()
puppy1.dog__sound()

#OOP code writing level 10:
class bank:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance
    def bankinfo(self):
        print("the name :",self.owner)
        print("the balance :",self.__balance) 
    def deposite(self,amount):
        self.__balance = self.__balance + amount
owner1= bank("hira",23000)  
owner1.deposite(500)
owner1.bankinfo()
 