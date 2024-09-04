# class laptop:
#     Price=""                    # class variable
#     Processor=""
#     Ram =""

# HP = laptop()
# DELL= laptop()
# LENOVO =laptop()
# HP.Price,Processor,Ram = 12000,"XYZ",8

# print(HP.Price,Processor)

# class laptop:
#     def __init__(self):
#         self.name="DELL"        # intance variable
#         self.qlf =""
#     def show(self):
#         print("name",self.name)
#         print("name",self.qlf)
# hp=laptop()
# dell=laptop() 
# leno=laptop() 

# hp.name="HPi"
# hp.qlf="b.e"

# dell.name="DELL"
# dell.qlf="b.com"
# hp.show() 
# dell.show()

# class fruit:
#     def __init__(self):
#         self.color="pink"
#     def display(self):
#         print(self.color,"is my favorite color")
    
# c_1=fruit() 

# c_1.color="blue"  
# c_1.display()    

# class Teacher:
#     def __init__(self,name,reg):
#         self.name =name
#         self.reg =reg
#     def display(self):
#         print("Name:", self.name)
#         print("reg.no:", self.reg)
# t1=Teacher("micle","272625")
# t1.display()

# class calculator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         print("total is",self.a+self.b)
# total=calculator(5,6)
# total.add()
class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def divi(self):
        print("total is",self.a/self.b)
total=calculator(100,60)
total.divi()

        
        



        