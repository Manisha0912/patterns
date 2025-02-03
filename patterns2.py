
# rhombus
n = 5
for i in range(n):
    print(" " * (n - i - 1) + "* " * n)
print()

# number increasing pyramid
for i in range(1, 5):
    for j in range(i):
        print(j + 1, end=" ")
    print()

# 1,0 triangle
for i in range(1, 6):
    for j in range(i):
        if (i + j) % 2 == 1:
            print("0", end=" ")
        else:
            print("1", end=" ")
    print()

