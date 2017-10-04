# python programe to find armstrong no.
#an armstrong no is the sum of the power of its digit is equals to the no. itself

def armstrong():
     num = int(input("Enter a number:-"))
     if num =='x':
        Break

     else:
      number = int (num)
      total = 0
      temp = number
      while temp > 0:
        digit = temp % 10
        total += digit **3
        temp //=10
     if number == total:

        print ("%d, is armstrong"%(num))

     else:
         print("%d, is not an armstrong"%(num))

     

if __name__ =='__main__':
    armstrong()


