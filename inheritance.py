# class tech():
#     def python(self):
#         print("am using python in backend")
# class frontend(tech):
#     def react(self):
#         print("am using react in frontend")

# obj_2=frontend()
# obj_2.python()

# obj_1= tech()
# obj_1.python()

# class mainbox():
#     def container(self):
#         print("box full of choco")
# class subox(mainbox):
#     def tinybox(self):
#         print("mini choco")
# T1=mainbox()
# T1.container()

# T2=subox()
# T2.container()    # single Inheritance oru function la irundhu inoru function ah call pandrathu

# class table():                # MULTI LEVEL INHERITANCE
#     def shop_1(self):
#         print("take a table")
# class book(table):
#     def shop_2(self):
#         print("take a book")
# class pen(book):
#     def shop_3(self):
#         print("take a pen")
        
# student=pen()
# student.shop_3()
# student.shop_2()
# student.shop_1()

# clint= book()
# clint.shop_1()

class maskan:
    def __init__(self):
        print("a")
    def welcome(self):
        print("welcome",self.name,self.qulfy)
         

class office(maskan):
    def __init__(self):
        super().__init__()
        print("b")
class employe():
    def __init__(self):
        super().__init__()
        print("do work")
    
z=employe()     
# x=maskan()
# y=office()
