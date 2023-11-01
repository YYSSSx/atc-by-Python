n = int(input())

a = [int(input()) for _ in range(n)]

res = 0
can = False
i = 0

while res<=n:
    i = a[i]-1
    res += 1
    if i == 1: 
        can = True
        break

if can: print(res)
else: print('-1')
