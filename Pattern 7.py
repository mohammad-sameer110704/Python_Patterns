def pattern7(n):
    if n < 0 :
        return "Invalid input, Enter number greater than 0 "
    for i in range(1,n+1):
        print(" "*(n-i)," *"*i)
n=int(input())
pattern7(n)