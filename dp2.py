# n = int(input())
# W = int(input())

# value = []
# weight = []

# for i in range(n):
#     x, y = map(int, input().split())
#     weight.append(x)
#     value.append(y)

# dp = [[0]*(W+1) for i in range(n+1)]

# for i in range(n):
#     for j in range(W+1):
#         if j>=weight[i]:
#             dp[i+1][j] = max(dp[i][j], dp[i][j-weight[i]]+value[i])
#         else:
#             dp[i+1][j] = dp[i][j]

# print(dp)
# print(dp[n][W])

n = int(input())
W_max = int(input())
W = []
V = []

dp = [[0] * 110 for _ in range(W_max+1)]

for _ in range(n):
    x, y = map(int, input().split())
    W.append(x)
    V.append(y)

for i in range(W_max+1):
    for j in range(n):
        if W[j] <= i:
            dp[i][j+1] = max(dp[i-W[j]][j]+V[j], dp[i][j])
        else:
            dp[i][j+1] = dp[i][j]

print(dp[W_max][n])



