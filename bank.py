import getpass

bank={'account':[1000],'name':['rohit'],'password':['rohit'],'balance':[1000]}

def bank1():
    Choice = int(input("""enter your choice 

1. New user 

2. Existing user

3. Exit

:"""))
    if Choice==1:
        adduser()
    elif Choice==2:
        login()
    else:
        exit1()


def adduser():
    Name=input('Enter user Name : ')
    while True:
        Password=getpass.getpass('Enter Password : ')
        Passwordc=getpass.getpass('Confirm Password : ')
        if Password==Passwordc:
            bank['name'].append(Name)
            bank['password'].append(Password)
            bank['account'].append(bank['account'][-1]+1)
            bank['balance'].append(input("Enter amount to credit :"))
            print('User Added Successfully')
            print('Note down the following information: ' )
            print("""Name = {0}
Password = {1} 
Account Number = {2}
Balance = {3}""".format(bank['name'][-1],bank['password'][-1],bank['account'][-1],bank['balance'][-1]))
            inp=input('You want to add more user (y/n) : ').lower()
            if inp=='n':
                bank1()
            elif(inp=='y'):
                adduser()
                break
        else:
            print('Wrong password Combination   ')
        

def debit(account):
    ind=bank['account'].index(account)
    debit=int(input('enter amount :'))
    if debit > bank['balance'][ind]:
        print('you enter higher ammount than available, your avl. ammount is ',bank['balance'][ind])
        login1(account)   
    else:    
        print(debit, 'is debited')
        bank['balance'][ind]-=debit
        print('remaining amount is :', bank['balance'][ind])
        ch1=input('you want to continue (Y/N')
        if ch1=='N' or ch1=='n':
            bank1()
        elif ch1=='y':
            login1(account)

def credit1(account):
    ind=bank['account'].index(account)
    credit=int(input('enter amount you want to credit :'))
    print(credit, 'is credited in your account')
    bank['balance'][ind]+=credit
    print('avl. Balance is :', bank['balance'][ind])
    ch1=input('you want to continue (Y/N')
    if ch1=='N' or ch1=='n':
        bank1()
    else:
        pass
        

def login():
    account=int(input('Enter Account No.: '))
    
    if account in bank['account']:
        i=3
        while i>=-1 :
            name=input('enter username : ')
            if name==bank['name'][bank['account'].index(account)]:
                
                login1(account)
                break
            elif i<0:
                bank1()
            else:
                i=i-1
                print('OOPS! Enter correct Account Number and Name Combination, session expire after {0} attemp'.format(i))
                print()
            
    else:
        print('There is no Account with this Account number')
        login()
def login1(acc):
    
    ind=bank['account'].index(acc)
    i=3
    while i>=0:
        password=getpass.getpass('Enter PassWord: ')
        if(password==bank['password'][ind]):   
                print("login success")
                c1=int(input("""1. debit
2. credit
3. check balance
4. exit
   :"""))
                if(c1==1):
                    debit(acc)    
                elif(c1==2):
                    credit1(acc)                                
                elif c1==3:
                    check(acc)
                elif c1==4:
                    bank1()
                else:
                    quit()
        elif i==0:
            bank1()      
        else:
            print()
            print('Enter Correct Password, {0} Chance left'.format(i))
            i-=1
            

def exit1():
    quit()
bank1()  

