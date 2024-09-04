class world:
    def __init__(self):
        self.__country="INDIA"     # __private
    
    def display(self):
        print(self.__country)
    
        
x=world()
x.display()
# x.country="pakistan"
# print(x.country)       