n=int(input("enter a number between 0 and 9:"))
squares = {i:"{} squared is {}".format(i, i**2) for i in range(10)}
print(squares[n])