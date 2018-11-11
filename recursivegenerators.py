#this program is an improvement of the program flattenNested.py
#it is applicable where the level of nesting is unknown and variable hence recursion is used.
def flatten(nested):
    try:
        try:
            nested+''
        except TypeError:           #element is not string-like
            pass                    #do nothing
        else:raise TypeError           #element is string-like
        for sublist in nested:
            for element in flatten(nested):          #recursion
                yield element
    except TypeError:return nested      #return string-like element as is
list(flatten([[[1], 2], 3, 4, [5, [6, 7]], 8]))
list(flatten(['foo', ['bar', ['baz']]]))

    

