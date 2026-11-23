def pattern2(n):
    if n < 1:
        return print("Invalid Input ,Enter a number greater than 0 ")
    for i in range (1,n+1):
        for j in range (1,i+1):
            print(j,end=" ")
        print("")
n = int(input("Enter a number greater than 0 : "))
pattern2(n)