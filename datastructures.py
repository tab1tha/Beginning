#this program illustrates the functioning of objects and data structures in python
#the exercises here are gotten from the udemy course called complete python bootcamp:go from zero to hero in python 3
x=9*10+1/4+2**4-6 #write mathematcal code that prints 10.25
print(x) 

print(4*(6+5))
print(4*6+5)
print(4+6*5)

print(25**0.5) #**0.5 is used to find squareroot
print( 5**2)  #**2 is used to find square
hello='hello'
print(hello[1])
print(hello[-1:])
print(hello[-1] + 'prints o')
print(hello[4])

lst=[]
for x in range(3):
    lst.append(0)
list3=[1,2,[3,4,'hello']]
list3[2][2]='goodbye'
print(list3)

list4=[5,3,4,6,1]
list4.sort()
print(list4)

d= {'simple_key':'yay'}
print(d['simple_key']) #print yay

d2={'k1':{'k2':'hello'}}
print(d2['k1']['k2']) #print hello

d3={'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0]) #print hello

d4={'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d4['k1'][2]['k2'][1]['tough'][2][0]) #print hello

list5=[1,2,2,33,4,4,11,22,3,3,2]
m=set(list5)
print(m)



