def myfun():
    x="my world"
    def cal(a,b):
       print("greater") if a>b else print("equal") if a==b else print("less")
    
    print(x)
    cal(20,20)
myfun()


