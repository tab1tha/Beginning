#__iter__ returns an iterator ; object with the method __next__ which can be 
# called without arguments
it= iter([1,2,3])
it.__next__()#the __next__ method returns the next value of the iterator,and
            # it raises a StopIteration exception when the values have been exhausted
print(next(it))#built-in convenience function equivalent to it.__next__()
print(next(it))#at this level,the third value in the object is returned
print(next(it))#at this level,StopIteration exception is raised since available 
# values in object have been exhausted. 

