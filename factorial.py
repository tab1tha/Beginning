def factorial(n):
    result=n
    for i in range(1,n):
        result = result*i #the number is multiplied by all the integers below it and above zero
        return result
