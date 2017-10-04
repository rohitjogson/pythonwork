
#python programe to check year is leap year or not
def main():
 year = int(input("enter a year-"))

 if (year % 4)== 0:

    if (year % 100) ==0:

        if (year % 400)==0:
            print("{0} is leap year" .format (year))

        else:
            print ("{0} is not leap year". format(year))

    else:
        print ("{0} is leap year".format(year))

 else:
    print ("{0} is not leap year" .format(year))

if __name__ == "__main__":
    main()



