class Myclass:
    def smeth():
        'static methods do not have an argument' #defined without self arguments
        print('this is a static method')
        smeth=staticmethod(smeth)#instantiation
    def cmeth(cls):
        'cls is the parameter associated with classic methods'
        print('this is a class method of',cls)
        cmeth=classmethod(cmeth)
Myclass.cmeth(cls)
Myclass.smeth()
   #for better functioning,refer to decorators.py 
Myclass.__docstring__()