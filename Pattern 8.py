def pattern8(n):
    if n < 0 :
        return print("Invalid input, Enter a number greater than 0 ")
    for i in range(n):
        print(" "*i," *"*(n-i))
n = int(input("Enter a number greater than 0 : "))
pattern8(n)
