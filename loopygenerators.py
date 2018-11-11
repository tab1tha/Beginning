#generator comprehension works in the same way as a list comprehension except that 
#a list is not created,allowing you to perform the operation step by step
g=((i+2)**2 for i in range(2,27))
next(g)
print(next(g))