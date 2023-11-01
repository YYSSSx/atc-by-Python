n = int(input())
a = list(map(int, input().split()))
A = int(input())

dp = [[0]*(n+1) for _ in range(A+1)]

dp[0][0] = 1

for i in range(A+1):
    for j in range(n):
        dp[i][j+1] = dp[i][j]
        if i>=a[j] : #and dp[i-a[j]][j]!=0:
            dp[i][j+1] += dp[i-a[j]][j]

print(dp[A][n])