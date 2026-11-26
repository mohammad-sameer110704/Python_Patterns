def pattern11(n):
    if n < 1 :
        return print("Invalid input, Enter a number greater than 0 ")
    for i in range(1,n+1):
        if i % 2 != 0 :
            for j in range(1,i+1):
                if j % 2 != 0 :
                    print("1",end=" ")
                else :
                    print("0",end=" ")
            print("")
        else:
            for j in range(i):
                if j % 2 == 0 :
                    print("0",end=" ")
                else:
                    print("1",end=" ")
            print("")
n = int(input("Enter a number greater than 0 : "))
pattern11(n)
