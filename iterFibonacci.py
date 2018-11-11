class Fibs:
    def __init__(self):
        self.a=0
        self.b=1
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        return self.a
    def __iter__(self):
        return self
        # It is recommended that iterators implement an __iter__ method of their
        #own in addition (returning self, just as I did here), so they themselves
        #  can be used directly in for loops.
fibs=Fibs() #fibs is an object from Fibs
for f in fibs: #this for loop finds the smallest number in the fibonacci sequence 
                #that is greater than 1000
    if f>1000:
        print(f)
        break
#an object implementing the __iter__ method is iterable,while the 
# object implementing next() is an iterator
