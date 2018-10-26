try:
    x=int(input('enter the numerator;'))
    y=int(input('enter the denominator;'))
    print(x/y)
except(ZeroDivisionError,ValueError,TypeError,NameError):
    print('the numbers you provided are bogus.Please try again')
    