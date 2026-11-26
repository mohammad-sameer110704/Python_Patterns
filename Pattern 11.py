def pattern11(n):
    if n < 1 :
        return print("Invalid input, Enter a number greater than 0 ")
    for i in range(1,n+1):
        for j in range(i):
            if j % 2 == 0 :
                pass
            if j % 2 != 0 :
                pass
n = int(input("Enter a number greater than 0 : "))
pattern11(n)
