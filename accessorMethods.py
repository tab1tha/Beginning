#accessor methods are used to retrieve or rebind  some attribute.
#in this program,getsize and setsize are the accessor methods of the attribute size.
class Rectangle:
    def __init__(self):
        self.height=10
        self.width=5
    def setsize(self):
        self.width,self.height=size
    def getsize(self):
        return self.width,self.height
r=Rectangle() #r is an instance of the class Rectangle
r.height=5
r.width=4
print(r.getsize)
