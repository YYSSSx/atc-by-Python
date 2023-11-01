n = int(input())


a = [list(map(int, input().split())) for _ in range(2)]

res = 0

for i in range(n):
    res = max(res, sum(a[0][0:i+1])+sum(a[1][i:n]))

print(res)