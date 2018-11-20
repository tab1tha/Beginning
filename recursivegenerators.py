#this program is an improvement of the program flattenNested.py
#it is applicable where the level of nesting is unknown and variable hence recursion is used.
def flatten(nested):
    try:
        try:nested+' '
        except TypeError:           #element is not string-like
            pass                    #do nothing
        else:raise TypeError           #element is string-like
        for sublist in nested:
            for element in flatten(sublist):          #recursion
                    yield element
    except TypeError:yield nested      #return string-like element as is
print(list(flatten([[[1], 2], 3, 4, [5, [6, 7]], 8])))
print(list(flatten(['foo', ['bar', ['baz']]])))

    
#If you followed the examples so far, you know how to use generators, more or less. You’ve seen that a
#generator is a function that contains the keyword yield. When it is called, the code in the function body is
#not executed. Instead, an iterator is returned. Each time a value is requested, the code in the generator is
#executed until a yield or a return is encountered. A yield means that a value should be yielded. A return
#means that the generator should stop executing (without yielding anything more; return can be called
#without arguments only when used inside a generator)