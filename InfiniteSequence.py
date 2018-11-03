#this program creates a sequence of infinite length
def check_index(key):
#ensures that the key is  a non negative integer
    if not isinstance(key,int):raise TypeError
    if key<0:raise IndexError
class ArithmeticSequence:
    def __init__(self,start=0,step=1):
        self.start=start
        self.step=step
        self.changed={}
    def __getitem__(self,key):
        "Get an item from the arithmetic sequence."
        check_index(key)
        try return self.changed[key] #has key changed?
        except KeyError:                #otherwise,
            return self.start+key*self.step #calculate value
    def __setitem__(self,key,value):
        "Change an item in the arithmetic sequence."
        check_index(key)
        self.changed[key]=value

#an arithmetic sequence is created;a sequence in which every number is greater than the previous number by a fixed amount.
