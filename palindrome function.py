def reverse(n):
    """ reverse(n):-> this is a function which gives reverse of any no."""

    r = 0
    while (n > 0): # loop until n is reverse
        t = n % 10 # seprate digit from n
        r = r*10 + t # adding to make no. reverse
        n//=10 # for removing lat digit from the no.
    return r # returning reverse no. which is stored in s
def main():
    """main()-> a function to check palindrome no."""
    n = int (input("\nenter a no."))
    print()
    r = reverse(n)
    print("reverse of ",n,"is=" , r)
    print()
    if n == r:
        print(n,"is a palindrome")
    else:
        print(n," is not a palindrome")

if __name__ == " __main__" :
    print("-----------------------------------------------------------------------------------")
    print()
while True:
    main()
    ch = input ("\n do you want to continue y/n - ")
    if ch.lower() == 'y' :
        pass #continue
    else:
        break
        print()
        print("----------------------------------------------------------------------------")
