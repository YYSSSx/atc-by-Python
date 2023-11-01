n = int(input())
a = list(map(int, input().split()))
m = list(map(int, input().split()))
A = int(input())

# dp = [-1]*(A+1)
# dp[0] = 0

# for i in range(n):
#     for j in range(A+1):
#         if dp[j]>=0:
#             dp[j] = m[i]
#         elif j<a[i] or dp[j-a[i]]<=0:
#             dp[j] =-1
#         else:
#             dp[j] = dp[j-a[i]] - 1
#     print(dp)
# print(dp)

dp = [[-1]*(A+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(A+1):
    for j in range(n):
        if dp[j][i]>=0:
            dp[j+1][i] = m[j]
        elif i>=a[j] and dp[j+1][i-a[j]]>0:
            dp[j+1][i] = dp[j+1][i-a[j]] - 1
        else:
            dp[j+1][i] = -1

if dp[n][A]>=0: print('Yes')
else: print('No')
for i in range(n+1): print(dp[i])

