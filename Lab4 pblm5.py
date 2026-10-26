n = int(input("Enter N: "))

a = 0
b = 1

while a < n:
    print(a)
    c = a + b
    a = b
    b = c