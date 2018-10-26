print('Welcome to the factorial manipulator')
value=int(input('Enter a number whose factorial you require;'))
def factorial(n): #this function calculates the factorial of the value put into it
    result=n
    for i in range(1,n):
        result = result*i #the number is multiplied by all the integers below it and above zero
    return result
print(factorial(value))
