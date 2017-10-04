
#python programe to check the input no is prime or not

def isprime(num):
    #prime no are greater than 1

    if num > 1:
        count=0

    #check for factors

        for i in range(2,num):

            if(num % i)==0:

                count+=1


        if count>0:
            print('number is not prime')
            
        else:
            print('num is prime')
            

def main():
    while True:
        num1=int(input('Enter the number : ').strip())
        isprime(num1)
        N=input('N-stop\nany for coninue').lower()
        if N=='n':
            break
        
if __name__ == "__main__" :
    main()
