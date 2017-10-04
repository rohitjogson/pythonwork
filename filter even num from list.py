def evenodd():
    evens = []
    odds = []

    n = int(input("enter a no-"))
# loop through every integer up to the maxnum
    for num in range (1,n+1 ):

        #test if number is even

        if num % 2 == 0 :
            evens.append(num)
        else:
            odds.append(num)


    print("evens",evens)
    print("odds",odds)

if __name__ == "__main__":
    evenodd()

