#a simple database to store personal information using shelve(.open,.close)
import sys,shelve
def store_person(db):
#ask user for data and store it in the shelf object
    pid=input('enter personal identification number:')
    person={}
    person[name]=input('enter name:')
    person[address]=input('enter your address:')
    person[mobile]=input('enter your mobile number:')
    db[pid]=person
def lookup_person(db):
    #query user for pid and desired field then provide requested information
    pid=input('enter personal identification number:')
    field=input('what do you want to know(name,age,mobile):')
    field=field.strip().lower() #ignore spaces and capitalisation differences
    print(field.capitalise()+':',db[pid][person][field])
def print_help():
    print('the available commands are:')
    print('store:stores information about a person')
    print('lookup:looks up a person using their id number')
    print('quit:save changes and exit')
    print('?:prints this message')
def enter_command():
    cmd=input('enter command(? for help):')
    cmd=cmd.lower().strip()#ignore spaces and capitalisation differences
    return cmd
def main():
    database=shelve.open('C:\\database.dat')
    try:
        while True:
            cmd=enter_command()
            if cmd=='store':
                store_person(datanbase)
            if cmd=='lookup':
                lookup_person(database)
            if cmd=='?':
                print_help()
            elif cmd=='quit':
                return
    finally:
        database.close()#if program terminates without closing the database properly,it may result in an utterly useless corrupt database file.
if __name__=='__main__':
    main()  #run the main function
#you can import this as a module and call the main() function from another program.
