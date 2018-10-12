#this program is meant to experiment the use of boolean values,indentation,if else and import in python
nam=input( "what is the name of your daughter?:")
import string
name=string.capwords(nam)
value =bool(name)
if value==True:
    print("your daughter  "+name+" is in safe hands")
else: 
    name=input( "what is the name of your daughter?:")
