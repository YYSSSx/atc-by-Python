n, d = map(int, input().split())

T = list(map(int, input().split()))

res = -1

for i in range(1,n):
    
    if T[i]-T[i-1]<=d:
        res = T[i]
        break

print(res)