#programe to check if a string is palindrome or not
#take input from user
def strpalindrome():
    return()

def main():
   my_str = input("enter a string:")

#make it suitable for caseless comparision

   my_str = my_str.casefold()

#reverse the string

   rev_str = reversed(my_str)

#check if string is equal to its reverse

   if my_str == rev_str:
    print("it is palindrome")
   else:
    print("it is not a palindrome")

if __name__ == '__main__':
    main()

