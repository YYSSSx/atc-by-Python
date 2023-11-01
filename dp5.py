n = int(input())
a = list(map(int, input().split()))
A = int(input())

dp =[[10010]*(n+1) for _ in range(A+1)]
dp[0][0] = 0

for i in range(A+1):
    for j in range(n):
        if i>=a[j]:
            dp[i][j+1] = min(dp[i-a[j]][j]+1, dp[i][j])
        else:
            dp[i][j+1] = dp[i][j]

print(dp[A][n])
print(dp)
