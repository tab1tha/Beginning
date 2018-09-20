#to print a sentence inputted by the user in a box
sentence=input('sentence: ')
textwidth=len(sentence)
boxwidth=textwidth+6
print('+' + '-'*(boxwidth-2) +'+')
print('|' + ' '*(boxwidth-2) +'|')
print('|' + sentence+ ' '*((boxwidth-2)-textwidth)+ '|')
print('|' + ' '*(boxwidth-2) +'|')
print('+' + '-'*(boxwidth-2) +'+')

print(sentence.strip())
