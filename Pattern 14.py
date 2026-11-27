# A
# AB
# ABC
# ABCD
# ABCDE

def pattern14(n):
    if n < 1 :
        return print("Invalid input, Enter a number greater than 0 ")
    for i in range(n):
        for j in range(i+1):
            print(chr(65+j),end=" ")
        print("")
n = int(input("Enter a number greater than 0 : "))
pattern14(n)
