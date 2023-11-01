n, y = map(int, input().split())

a = -1
b = -1
c = -1

for i in range(n+1):
    for j in range(n+1-i):
        if y == 10000*i + 5000*j + 1000*(n-i-j):
            a = i
            b = j
            c = n-i-j

print(a, b, c)