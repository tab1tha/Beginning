#a demonstration of the various list methods
yam=[1,5,9,3,2,6,4,7,10,45,29]
yam.append(4) #append
print(yam)

yam1=yam.copy()#copy
print(yam1)

yam1.clear()#clear
print(yam1)

print(yam.count(4))#count

a=[0,4,1]#extend
yam.extend(a)
print(yam)

print(yam.index(4))#index

yam.insert(0,100)#insert
print(yam)

print(yam.pop())#pop
print(yam)

yam.remove(4)#remove
print(yam)

yam.reverse()#reverse
print(yam)

yam.sort()
print(yam)