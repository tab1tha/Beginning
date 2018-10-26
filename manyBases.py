class Calculator:
    def calculate(self,expression):
        self.value=eval(expression)
class Talker:
    def talk(self):
        print("the value is {}".format(self.value))
class TalkingCalculator(Calculator,Talker):     #a class with more than one superclass i.e two superclasses;Calculator,Talker
    pass
tc=TalkingCalculator()
print("This calculator is ready to serve you")
ex=str(input("enter an expression:"))
tc.calculate(ex)
hasattr(tc,talk) #optional line to check if the instance tc has an attribute called talk
callable(getattr(tc,calculate,None))#optional line to check if attribute is callable
setattr(tc,name,"Mr Gumby")#optional line showing the use of setattr().this line does tc.name="Mr Gumby"
tc.talk()
print('thank you for your time')
#this program also efficiently implements the functions of a calculator