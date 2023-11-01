n = int(input())
num = list(map(int, input().split()))
A = int(input())

dp = [[0]*(n+1) for _ in range(A+1)]
dp[0][0] = 1


for i in range(A+1):
    for j in range(n):
        dp[i][j+1] = dp[i][j]
        if i>=num[j]:
            if(dp[i-num[j]][j]==1):
                dp[i][j+1] = 1

if dp[A][n] == 1: print('Yes')
else: print('No')
#print(dp)