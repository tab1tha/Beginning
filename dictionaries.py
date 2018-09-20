#program to demonstrate how dictionaries can be manipulated
x=[('Alice',234),('Spring','456'),('Regime','678'),('Farm','234')]
d=dict(x)
print(d)
r={'Alice':243}
d.update(r)
print(d)
print(d.pop('Farm'))
print(d.popitem())
print(d)
print(d.values())
print(d.get('stone','NA'))
print(d.keys())
print(d.items())
d.setdefault('name',100)
print(d)
from copy import deepcopy
b=deepcopy(d)
b['Alice']=908
print(b)
print(d)
b.clear()
print(b)
c=d.copy()
del c['Spring']
print(len(c))
print('Spring' in c)
print(d)