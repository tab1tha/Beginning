#this program demonstrates the use of the dir function
import copy
print(dir(copy))
#the dir function list all the attributes of an object;
#hence all classes,functions,variables etc of a module(in this case,the copy module)

#it should be noted that the double underscores in front of some attributes is an indicator that 
# they are not meant to be used outside the module

#list comprehension can be used to filter out these;
print([n for n in dir(copy) if not n.startswith('_')])

#the __all__ attribute contains a list of the attrihutes that will be imported if 
#from copy import* is run
#i.e it defines the public interface of the module.
print(copy.__all__)