#first creat a new file...
creat_file="phonebook.txt"
file=open(creat_file,"a")
file.close

#welcoming...!
print("welcome to phonebook! \n please enter your name:")
name=input()
print('Hello', name ,'How can I help you?')

def introduction():
    #explain how to input what you want to find
    choose=input('''please select where you want to go by choosing (A/S/R/X/D):
     A=All numbers
     S=Save new contact
     R=search contacts
     D=Delet contacts
     X=Exit
     ''').upper()
    if choose =='A':
        file=open(creat_file,'r')
        readfile=file.read()
        if len(readfile) == 0 :
            print('Oops!your list is empty')
        else:
            print(readfile)
        p=input('Press Enter to Continue...')
        introduction()
    elif choose == 'S':
        save_contact()
        p=input('Press Enter to Continue...')
        introduction()
    elif choose =='R':
        search_contacts()
        p=input('Press Enter to Continue...')
        introduction()
    elif choose =='D':
        delet_contact()
        p=input('Press Enter to Continue...')
        introduction()
    elif choose =='X':
        print('Thanks for using phonebook.Have a Great Day!')
        p=input('Press Enter to Continue...')
        introduction()
    else:
        print('Error!please try again')
        p=input('Press Enter to Continue...')
        introduction()


def save_contact():
    flag=False
    fullname=input('please enter the fullname:').capitalize()
    file=open(creat_file,'r')
    r=file.readlines()
    for line in r:
        if fullname in line:
            flag=True
            choose=input('''Do you want to add this number to existing one?
             (if yes,click Y,if no click N):
             ''').upper()
            if choose == 'Y':
                phonenumber=input('please enter the number:')
                con=('['+line+','+ phonenumber +']')
                file=open(creat_file,'w')
                file.write(con)
                file.close()
                print('addedd successfully')
            elif choose == 'N':
                phonenumber=input('please enter the number:')
                contact=('[' +fullname+' , '+phonenumber+']\n')
                file=open(creat_file,'a')
                file.write(contact)
                file.close()
                print('successfully added!')
    if not flag:
        phonenumber=input('please enter the number:')
        contact=('[' +fullname+' , '+phonenumber+']\n')
        file=open(creat_file,'a')
        file.write(contact)
        file.close()
        print('successfully added!')

def search_contacts():
    search=input('enter the name you want to find:').capitalize()
    file=open(creat_file,'r')
    file_c=file.readlines()
    for line in file_c:
        if search in line:
            print(line)
            break
        if line not in file_c:
            print('Nothing found!')
            break


def delet_contact():
    removing_name=input('enter the name you want to remove:').capitalize()
    file=open(creat_file,'r')
    file_con=file.readlines()
    for line in file_con:
        if removing_name not in line:
            file=open(creat_file,'w')
            file.write(line)
            file.close()
        print('removed successfully')
        break
introduction()