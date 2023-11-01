N = int(input())

res = 1000
for i in range(N, 920):
    x = str(i)
    x1 = int(x[2])
    x2 = int(x[1])
    x3 = int(x[0])

    if x1==x2*x3:
        res = min(res, i)

print(res)


