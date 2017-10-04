n=int(input('Enter any number: '))
if n%2!=0:
    n=n+1
for i in range(n):
    for j in range(n):
        if (i==int(n/2)) or j==int(n/2) or ((i==0)and (j>=int(n/2))) or ((j==0)and (i<=int(n/2))) or ((j==n-1)and (i>=int(n/2))) or ((i==n-1)and (j<=int(n/2))):
            print('*',end='')
        else:
            print(' ',end='')
    print()
