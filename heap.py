#a heap is a data structure that is a type of priority queue i.e. it adds various 
#objects in an arbitrary order at the same time.there is also a possibility of finding
#(and removing) the smallest element in the heap.
from heapq import *
from random import shuffle
data=list(range(10))
shuffle(data)
heap=[]
for n in data:
    heappush(heap,n)
print(heap)
heappush(heap,0.5)
print(heap)
#the heap property:  the element at position i is always greater than 
# the one in position i // 2 
heappop(heap) #pops out the smallest element.
print(heap)
heapreplace(heap,0.5) #pops out the smallest element and replaces it with 0.5
print(heap)
heapreplace(heap,10) # this function returns the smallest element.
print(heap)#prints outvthe modified heap.


