#deques are useful when elements have to be removed in the order which they were added.
#deques are double-ended queues
from collections import deque
q=deque(range(5))
q.append(5)
q.appendleft(6)
print(q)
q.rotate(3)#moves elements in queue by adding three positions to their index such 
#that elements go round the ends of the queue.
print(q)
q.rotate(-1)#elements are moved one position to the left of their present positions.
print(q)
q.pop()#pops last element on the right
q.popleft()#pops first element in queue #this cannot be done with a list.
print(q)
