# python programe to find the factorial of a no. provided by the user
def factorial (n) :
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1) # recursive call


var = int (input (" enter a number-"))
print(factorial(var))

