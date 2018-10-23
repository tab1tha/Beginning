class Person:
    def setname(self,name):
        self.name=name
    def getname(self):
        return self.name
    def greet(self):
        print("hello world.my name is {}".format(self.name))
v=Person()
v.setname("John Paul")
print(v.getname())
v.greet()