#consider a list of lists,this program uses the flatten function to create one big
#list containing all the elements in the nested list;
#let the nested list be called nested
def flatten(nested):
    for sublist in nested:
        for element in sublist: #this statement and the preceding one imply that 7 will not be printed.
            yield(element) #returns many values;one at a time
nested=[[1,4],[2,3],[5],[7,8]]
print(list(flatten(nested)))
