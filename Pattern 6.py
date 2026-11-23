def pattern6(n):
    if n < 1 :
            return "Invalid Input, Enter a number greater than 0 "
    for i in range(1,n+1):
        for j in range(i):
            print(i,end=" ")
        print("")
n = int(input("Enter a number greater than 0 : "))
pattern6(n)
