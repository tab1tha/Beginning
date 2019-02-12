

f=open(r'C:\Users\Tabi\Desktop\sometext.txt')
print(f.read(5)) #reads first five characters(including whitespaces if any)
print(f.read(2)) #reads next two characters
f.seek(0) #takes cursor place back to the beginning of the script
print(f.read(2)) #reads next two characters
print(f.read())  #continues from where previous read() stopped till the end
f.close()

f=open(r'C:\Users\Tabi\Desktop\sometext.txt')
for i in range(3):
    print(str(i)+':'+ f.readline(),end='') #readline reads a whole line at a time.
f.close()

f=open(r'C:\Users\Tabi\Desktop\sometext.txt')
import pprint   #prettyprint
pprint.pprint(f.readlines()) #readlines() reads all the lines at once
f.close() #always close files at the end of the modification

#the write method of files
f=open(r'C:\Users\Tabi\Desktop\sometext.txt','w+')
f.write('this\nis no\nhaiku')
print(f.read())
f.close()

