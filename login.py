#check user login details
pineapple=[['Yolo','54321'],['Looy','32541'],['Oloy','12354']]
username=input('enter username:')
pin=input('enter pin:')
if [username,pin] in pineapple:print('Access granted')
pineapple[1]='Peter' #testing replacement in a list
print(pineapple)
del pineapple[0:2] #testing deletion of items in a list
print(pineapple)