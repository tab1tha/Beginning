#this is a follow up from the program accessorMethods.py
#however,magic methods are used here instead
class Rectangle:
    def __init__(self):
        self.height=0
        self.width=0
    def __setattr__(self,name,value):
        if name==size:
            self.height,self.width=value
        else:
            self.__dict__[name]=value
    def __getattr__(self,name):
        if name==size:
            return self.height,self.width
        else:
            raise AttributeError()
r=Rectangle
Rectangle.__setattr__(r,name==size,value=(45,22))
Rectangle.__getattr__(r,size)


