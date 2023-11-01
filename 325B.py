n = int(input())
W = []
X = []

for i in range(n):
    x, y = map(int, input().split())
    W.append(x)
    X.append(y)

ans = 0
for i in range(24):
    a = 0
    for j in range(n):
        if (i+X[j])%24>=9 and (i+X[j])%24 < 18 :
            a+=W[j]
        
            
    ans = max(a, ans)

print(ans)