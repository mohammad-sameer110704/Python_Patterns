def pattern1(n):
    if n < 1:
        return "Invalid input, Number is Less than 1"
    for i in range (n):
        print("* "*n)
n = int(input("Enter a number greater than 0 : "))
pattern1(n)