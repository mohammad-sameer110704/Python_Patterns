def pattern13(n):
    if n < 0 :
        return print("Invalid input, Enter a number greater than 0 ")
    a = 1
    for i in range(1,n+1):
        for j in range(i):
            print(a,end=" ")
            a += 1
        print("")
n = int(input("Enter a number greater than 0 : "))
pattern13(n)    
