#this program finds the largest value among values from the user
x=int(input("enter the value of x:"))
y=int(input("enter the value of y:"))
z=int(input("enter the value of z:"))#input values of various variables
if (x>y and x>=z):
        print('{} is the largest number'.format(x) )
elif(y>x and y>z):
        print('{} is the largest number'.format(y) )
elif(z>x and z>y):
        print('{} is the largest number'.format(z) )
else:
    print('all three numbers are the same')
        
k=x+y+z
status="small" if(k<10) else "large"
print(status)