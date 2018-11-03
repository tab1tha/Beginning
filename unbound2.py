#here,instead of calling the unbound version of the superclass constructor,the super function is used.
#super takes the present class and instance as arguments:super(Birdsong,bs) or super(Birdsong,self)
#any method you call on the returned object will be fetched from the superclass rather than the current class
#the arguments are optional
class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('Aaaah ...')
            self.hungry = False
        else:
            print('No, thanks!')
class SongBird(Bird):
        def __init__(self):
            super().__init__()
            self.sound = 'Squawk!'
        def sing(self):
            print(self.sound)
sb = SongBird() 
sb.sing()
sb.eat()
sb.eat()
#What super actually does is return a super object, which will take care of
#method resolution for you. When you access an attribute on it, it will look through all your superclasses
#(and super-superclasses, and so forth) until it finds the attribute, or raises an AttributeError.