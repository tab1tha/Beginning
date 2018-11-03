#__init__ is the constructor and __del__ is the destructor
#the constructor __init__ differs from the method init() in that it is called 
#immediately after the object is created
class Foobar:
    def __init__(self):
        self.somevar=42
f=Foobar()
print(f.somevar)

#however,arguments can be added to the constructor as such;
class Foobar:
    def __init__(self,value=42):
        self.somevar=value
f=Foobar()
print(f.somevar)

