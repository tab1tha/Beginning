#a demonstration of the various string methods
rain="the sun shAll soon shine"
print(rain.center(40,"*")) #center

print(rain.find('shine')) #find
print(rain.find('the'))

print("//".join(rain))#join

print(rain.lower())#lower

print(rain.replace("u","oo"))#replace

print("whiter;than;white".split(';'))#split
print(rain.translate('so''zu'))

