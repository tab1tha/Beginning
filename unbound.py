#When you retrieve a method from an instance, the self argument of the method
#is automatically bound to the instance (a so-called bound method). You’ve seen several examples of that.
#However, if you retrieve the method directly from the class (such as in Bird.__init__), there is no instance
#to which to bind. Therefore, you are free to supply any self you want to. Such a method is called unbound.
#this program illustrates how to call an unbound superclass in order to include methods that were overwritten
class Bird:
    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry:
            print("Ahhh....")
            self.hungry=False
        else:
            print("No,Thanks")
b=Bird()
b.eat()
b.eat()

class Birdsound(Bird):  #a subclass of Bird which inherits the eat() attribute but overwrites the constructor
    def __init__(self):
        #Birdsound constructor must call the constructor of its superclass in order to make sure that the basic initialisation takes place.
        Bird.__init__(self)#the first way of doing this is by calling the unbound version of the constructor of the superclass
        self.sound='Squawk'
    def sing(self):
        print(self.sound)
bs=Birdsound()
bs.sing()
bs.eat() #without line 17,this produces an attributeError exception:'Birdsound'has no attribute 'hungry'
#this is because,'hungry' is defined in the constructor of class Bird,however its constructor is overwritten in the subclass Birdsound.hence the attribute is not defined in bs.

