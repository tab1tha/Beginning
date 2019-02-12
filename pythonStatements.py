#these exercises are from my second assessment on the zero to hero udemy course
st='Print only words that start with s in this sentence'
for word in st.split():
    if word[0]=='s':
        print(word)

m=[x for x in range(0,11) if x%2==0]#all even numbers from zero to ten
print(m)

# a list comprehension is used to create a list of al numbers between 1 and 50 
#that are divisible by 3
print([num for num in range(1,51) if num%3==0])

st2='Print every word in this sentence that has an even number of letters'
for word in st2.split():
    if len(word)%2==0:
        print(word)

for v in range(0,101):
    if v%5==0 and v%3==0:
        print('FizzBuzz') #for multiples of 3 and 5
    elif v%3==0:
        print('Fizz') #for multiples of 3 only
    elif v%5==0:
        print('Buzz') #for multiples of 5 only
    else:
        print(v) #p
        
st3='Create a list of the first letters of every word in this string'

first=[word[0] for word in st3.split() ]
print(first)

