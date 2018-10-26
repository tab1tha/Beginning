try:
    x=int(input('enter the numerator;'))
    y=int(input('enter the denominator;'))
    print(x/y)
except ZeroDivisionError:
    print("the second number should not be zero")
except ValueError:
    print("that was not a number,was it?")
    