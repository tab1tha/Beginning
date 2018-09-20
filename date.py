#program to print out the date using information from user
month_name=['January', 'February', 'March', 'April', 'May', 'June',
 'July', 'August','September', 'October', 'November', 'December']
ordinal=['st','nd','rd']+17*['th']+['st','nd','rd']+7*['th']+['st']
month=input('month(1-12):')
day=input('day(1-31):  ')
year=input('year:')
mnumber=int(month)
m=month_name[mnumber-1]
dnumber=int(day)
d=day+ordinal[dnumber-1]
print(d+' '+m+' '+year)