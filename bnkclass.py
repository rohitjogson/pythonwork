import getpass
import json
class mybank:
    'this class have all functionality of the banking system'
    f=open('jsondata','r+')
    bank=json.load(f)
    f.close()
    def __init__(self):
        self.details={}
    def bank1(self):
        self.Choice = int(input("""enter your choice 

1. New user 

2. Existing user

3. Exit

:"""))
        if self.Choice==1:
            self.adduser()
        elif self.Choice==2:
            self.login()
        else:
            self.exit1()


    def adduser(self):
        Name=input('Enter user Name : ')
        while True:
            Password=getpass.getpass('Enter Password : ')
            Passwordc=getpass.getpass('Confirm Password : ')
            if Password==Passwordc:
                mybank.bank['name'].append(Name)
                mybank.bank['password'].append(Password)
                mybank.bank['account'].append(mybank.bank['account'][-1]+1)
                mybank.bank['balance'].append(input("Enter amount to credit :"))
                print('User Added Successfully')
                print('Note down the following information: ' )
                print("""Name = {0}
Password = {1} 
Account Number = {2}
Balance = {3}""".format(mybank.bank['name'][-1],mybank.bank['password'][-1],mybank.bank['account'][-1],mybank.bank['balance'][-1]))
                inp=input('You want to add more user (y/n) : ').lower()
                if inp=='n':
                    f=open('jsondata','r+')
                    json.dump(mybank.bank,f)
                    f.close()
                    self.bank1()
                elif(inp=='y'):
                    
                    f=open('jsondata','r+')
                    json.dump(mybank.bank,f)
                    f.close()
                    self.adduser()
                break
            else:
                print('Wrong password Combination   ')
        

    def debit(self,account):
        ind=mybank.bank['account'].index(account)
        debit=int(input('enter amount :'))
        if debit > mybank.bank['balance'][ind]:
            print('you enter higher ammount than available, your avl. ammount is ',mybank.bank['balance'][ind])
            self.login1(account)   
        else:    
            print(debit, 'is debited')
            mybank.bank['balance'][ind]-=debit
            print('remaining amount is :', mybank.bank['balance'][ind])
            ch1=input('you want to continue (Y/N')
            if ch1=='N' or ch1=='n':
                f=open('jsondata','r+')
                json.dump(mybank.bank,f)
                f.close()
                self.bank1()
            elif ch1=='y':
                f=open('jsondata','r+')
                json.dump(mybank.bank,f)
                f.close()
                
                self.login1(account)

    def credit1(self,account):
        ind1=mybank.bank['account'].index(account)
        credit=int(input('enter amount you want to credit :'))
        print(self.credit, 'is credited in your account')
        mybank.bank['balance'][ind1]+=credit
        print('avl. Balance is :', mybank.bank['balance'][ind1])
        ch1=input('you want to continue (Y/N')
        if ch1=='N' or ch1=='n':
            f=open('jsondata','r+')
            json.dump(mybank.bank,f)
            f.close()
            self.bank1()
        else:
            f=open('jsondata','r+')
            json.dump(mybank.bank,f)
            f.close()
            pass

    def login(self):
        account=int(input('Enter Account No.: '))
    
        if account in mybank.bank['account']:
            i=3
            while i>=-1 :
                name=input('enter username : ')
                if name==mybank.bank['name'][mybank.bank['account'].index(account)]:
                
                    self.login1(account)
                    break
                elif i<0:
                    self.bank1()
                else:
                    i=i-1
                    print('OOPS! Enter correct Account Number and Name Combination, session expire after {0} attemp'.format(i))
                    print()
            
        else:
            print('There is no Account with this Account number')
            self.login()
    def login1(self,acc):
    
        ind=mybank.bank['account'].index(acc)
        i=3
        while i>=0:
            password=getpass.getpass('Enter PassWord: ')
            if(password==mybank.bank['password'][ind]):   
                print("login success")
                c1=int(input("""1. debit
2. credit
3. check balance
4. exit
   :"""))
                if(c1==1):
                    self.debit(acc)    
                elif(c1==2):
                    self.credit1(acc)                                
                elif c1==3:
                    self.check(acc)
                elif c1==4:
                    self.bank1()
                else:
                    quit()
            elif i==0:
                self.bank1()      
            else:
                print()
                print('Enter Correct Password, {0} Chance left'.format(i))
                i-=1
            
    def check(self,account):
        ind1=mybank.bank['account'].index(account)
        print('avl. Balance is :', mybank.bank['balance'][ind1])
        
        
    def exit1(self):
        quit()
    f.close()

obj=mybank()
obj.bank1()

    
        
        
