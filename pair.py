#this program demonstrates various ways of grouping names from two lists

girls = ['elice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
print([b+'+'+g for b in boys for g in girls if b[0] == g[0]])
#groups names that begin with the same letter of the alphabet

print([(g,b) for b in boys for g in girls])

l=list(zip(boys,girls))
print(l)