import re

#mail id generator--------------------
name1=input("Enter first name: ")
name2=input("Enter last name: ")
l=["tejteja","tej teju","tejteja097","teju"]
while 1:
    un=input("Enter prefered username: ")
    if un not in l :
        if un.islower()and re.search(r"[^A-z!@#$%^&*]",un):
            l.append(un)
            print("Your mail id is: "+un+"@blackmail.com")
            break
        else:
            print("use only small letters and numerics")
    else:
        print("Entered user name alreay exists! please try a new name")
        
        
#password genarator--------------------
while 1:
    pas=input("Enter a strong password: ")
    match=re.search(r"[0-9A-Za-z!@#$%^&*?,.]{8,}",pas)
    if match:
        while 1:
            pas2=input("re-enter the password: ")
            if pas2==pas:
                print("password created successfully!")
                break
            else:
                print("password missmatch! please re enter the password")
        break
    else:
        print("password must cointain a capital letter, number,special character and length should be minimum 8 characters")
print("blackmail created successfully..............!!")
print("\tThankyou for using blackmail..!!")
