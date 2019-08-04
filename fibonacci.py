n = int(input("Type the length of the sequence: "))
x, y = 0, 1
z = x+y
for i in range(n):
    print(z)
    x, y = y, z
    z = x + y
