# program to display all the armstrong number in which interval which is given by user
# take input from user
def arm():
     'this function take two integer and print the armstrong number b\w that range '
     lower = int(input("enter lower range:"))
     upper= int(input("enter upper range:"))
     list1=[]
     for num in range(lower, upper+1):
          sum1=0
          
          temp = num
          while temp > 0:
             digit = temp % 10
             sum1 +=digit**3
             temp=temp//10
             
          if num == sum1:
             list1.append(num)
     if len(list1)>0:
        print(list1)
     else:
        print('there is no armstrong number')
if __name__=='__main__':
     
     arm()




