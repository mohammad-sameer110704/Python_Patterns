def pattern7(n):
    if n < 0 :
        return print("Invalid Input ,Enter a number greater than 0 ")
    for i in range(1,n+1):
        print(" "*(n-i)," *"*i)
n = int(input("Enter a number greater than 0 : "))
pattern7(n)