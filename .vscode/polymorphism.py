# class Animal:      # one function bt can we use muli time and override the result its calld pylymphsm
    
#     def sound(self):
#         print("Animal make a sound")
# class Dog(Animal):
#     def sound(self):
#         print("DOG BARKS")
# class Bird(Animal):
#     def sound(self):
#         print("Birds sing")
# # a=Animal()  
# # a.sound()

# c=Bird()
# c.sound()

# class Shape:
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b
        
#     def area(self):
#         print("result",self.l*self.b)
# class Rectangle(Shape):
#     def area(self):
#         print("area of the rectangleis",self.l*self.b)
# # T=Shape(5,6)
# # T.area()
# T2=Rectangle(7,8)
# T2.area()

# class Person:
#     def __init__(self,name):
#         self.name=name
        
# class Student(Person):
#     def __init__(self,name,grade):
#         super().__init__(name)
#         self.grade=grade
        
#     def display(self):
#       print(self.name,self.grade)

        
# x=Student("taj",2)
# x.display()

# class vehicle:
#     def start(self):
#         print("vehicle started")
# class car(vehicle):
#         def start(self):
#             print("Car started")
# a=car()
# a.start()

class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
class manager(employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def display(self): 
        print(self.name,self.salary,self.department)
        
a=manager("arun",20000,"IT")
a.display()
        
    
    

    




    
    
    
