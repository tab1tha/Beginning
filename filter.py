class Filter:
    def init(self):
        self.blocked=[]
    def filter(self,sequence):
        return[ x for x in sequence if x not in self.blocked]

foo=Filter()
foo.init()
print(foo.filter([1,2,3]))

class SPAMFilter(Filter):
    def init(self):
        self.blocked=["SPAM"]
f=SPAMFilter()
f.init()
print(f.filter(["SPAM","PAM","SAM","eggs","spam"]))


        