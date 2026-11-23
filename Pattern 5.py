def pattern5(n):
    if n < 1 :
        return print("Invalid Input ,Enter a number greater than 0 ")
    for i in range(n):
        print("*"*(n-i))
n = int(input("Enter a number greater than 0 : "))
pattern5(n)