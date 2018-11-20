#this program is a improvement of the program staticClassicMethods.py
#decorators are used as wrappers to wrap methods such that they can be used without
#instantiating the class
#they are placed above the function or method and are executed in reverse order.
class Myclass:
    'hey,I am a class' #docstring containing information about the class
    @staticmethod
    def smeth():
        print('this is a static method')
    @classmethod
    def cmeth(cls):
        print('this is a class method of',cls)
Myclass.smeth()
Myclass.cmeth()
print(Myclass.__doc__)  #displays the docstring.