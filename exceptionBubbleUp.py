#if an exception is raised in a program and it isn't handled there,the exception 
#propagates(bubbles up) to the place where the function is called.if it is still 
#not handled,it keeps 'bubbling up' right up to the global scope and if it not 
#handled there,the program halts with a stack trace.
def faulty():
    raise Exception('something went wrong')
def ignore_exception():
    faulty()
def handle_exception():
    try:
        faulty()
    except:
        print('exception handled')
handle_exception() #handles exception at the place where function is called
ignore_exception() #causes program to halt with a stack trace