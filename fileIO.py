with open('sometext1.txt',mode='w') as fil:
    fil.write('hello how are you doing huh?')
with open('sometext1.txt',mode='r') as fil:

    contents=fil.read()
print(contents)