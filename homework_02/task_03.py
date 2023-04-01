x = 0
y = 1
N = int(input())
while y <= N:
    y = 2 ** x
    print(y)
    x += 1
if y >= N:
    print(y, end=" ")

