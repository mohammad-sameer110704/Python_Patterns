def pattern2(n):
    if n < 1:
        return print("Invalid Input ,Enter a number greater than 0 ")
    for i in range (1,n+1):
        print("* "*i)
n = int(input("Enter a number greater than 0 : "))
pattern2(n)