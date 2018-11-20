#send is used to input values into a generator while it is still running.however,
#the generator should have run at least once(yielded one value).
#if 'send' must be used on a newly started generator,it should be used with parameter  None
def repeater(value):
    while True:
        new=(yield value)#yield expressions should always be enclosed in parentheses if the return value has to be used in some way.
        if new is not None:value=new
r=repeater(42)
r.send(None)#here the generator is considered as just started since it has not yielded any value yet.
#Hence if something other than None is sent to it,an error will be produced.
print(r.__next__())
print(r.__next__())
r.send("hi")    #this changes the generator value to the string hi
print(r.__next__())

#the throw method e.g. r.throw is used to raise exceptions in the generator,at the level of yield.
# it is called with an exception type,an optional value,and a traceback object.

#the close method (called with no arguments) is used to stop the generator.
#it raises a GeneratorExit exception at the yield point.Hence wrap up code(if any),
#should be enclosed in a try/finally statement.