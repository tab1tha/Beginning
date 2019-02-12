userstatus=input('Are you new or a veteran?')
userstatus.lower()
users=[]
if userstatus=='new':
    username=input('Can I please know your name?:')
    users.append(username)
    userstatus='veteran'
    print(f'Welcome {username},to the guessing game.Enter a number between 1 and 100 inclusive')
    print('The closer your guess is to the number chosen by me,the warmer it will be and vice versa')
    print('you win when you can guess the number in my head.No worries,I am here to help.')

elif userstatus=='veteran':
    print('Welcome back')
trial=0
from random import randint
mynum=randint(1,100)
print(mynum)

yournum=int(input('Enter any number between 1 and 100:'))
trial+=1
tried=[]
tried.append(yournum)
if yournum<1 or yournum>100:
    print('OUT OF BOUNDS')

x=yournum-mynum

if abs(x)<=10:
    print('warm')
elif abs(x)>10:
        print('cold')
    

while(yournum!=mynum):
    yournum=int(input('Enter any number between 1 and 100:'))
    trial+=1
    tried.append(yournum)
    x=yournum-mynum
    if abs(tried[-2]-mynum)>abs(tried[-1]-mynum): 
    #if you are getting closer to my number
        print('warmer')
        continue
    elif abs(tried[-2]-mynum)<=abs(tried[-1]-mynum) :
        print('colder')
        continue
if yournum==mynum:
    print(f'You guessed RIGHT after trying {trial} times')