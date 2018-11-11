#accessor methods are used to retrieve or rebind  some attribute.
#in this program,getsize and setsize are the accessor methods of the attribute size.
class Rectangle:
    def __init__(self):
        self.height=0
        self.width=0
    def setsize(self,size):
        self.width,self.height=size
    def getsize(self):
        return self.width,self.height 
    size=property(getsize,setsize) #optional #a property is an attribute which is defined by accessors
r=Rectangle() #r is an instance of the class Rectangle
r.setsize((130,35))#if size is defined as a property,this line will instead be written as r.size=130,35
print(r.width)
r.width=4
r.height=5
a=r.getsize()#if size is defined as a property,this line will instead be written as r.size
print(a)