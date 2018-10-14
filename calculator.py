n=int(input('Enter a number:'))
assert n,'you have not entered a number'
m=int(input('Enter another number:'))
assert m,'you have not entered a number'

#addition
print('their sum is {}'.format(m+n))
#multiplication
print('their product is {}'.format(m*n))
#comparison
if(n>m):
    print('{} is larger than {}'.format(n,m))
    big=n
    small=m
    print('{} divided by {} is {}'.format(big,small,big//small))
    print('{} minus {} is {}'.format(big,small,big-small))

if(m>n):
    print('{} is larger than {}'.format(m,n))
    big=m
    small=n
    print('{} divided by {} is {}'.format(big,small,big//small))
    print('{} minus {} is {}'.format(big,small,big-small))


elif(m==n):
    print('The numbers are equal to each other')
    print('{} divided by {} is 1'.format(m,n))