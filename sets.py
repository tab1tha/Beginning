a={1,2,3,4,5}
b={1,6,7,8,9}
print(a.union(b))
#since sets are meant for membership,repetitions are ignored.
print(a.intersection(b))
print(a|b) #or
print(a&b) #and
c=a&b
print(c.issubset(a))  
print(c.issuperset(a))  
print(c<a)  
print(a.difference(b))
print(a-b)
print(a.symmetric_difference(b))
print(a^b)
d=a.copy()
print(d is a)
#For more information, see the section about set types in 
# the Python Library Reference.

print(a.add(frozenset(b)))
#The frozenset constructor creates a copy of the given set. It is useful whenever you want to use a set either
#as a member of another set or as the key to a dictionary.