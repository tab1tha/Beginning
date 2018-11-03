#in this program,a subclass is created which inherits the attributes of the built in class;list.
class Counterlist(list):
    def __init__(self,*args):
        super().__init__(*args)#the super function is used to initialise the superclass(es)
        self.counter=0
    def __getitem__(self, index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)
cl=Counterlist(range(10))
print(cl)
cl.counter #this value starts from zero and increments itself whenever a value in the list is accessed.e.g.
            #after performing a calculation such as cl[4]+cl[5],cl.counter=2 since the list was accessed twice.
