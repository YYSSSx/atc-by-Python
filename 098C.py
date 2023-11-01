n = int(input())
s = input()

res = n
W = [0]*300010
E = [0]*300010

for i in range(n):
    if s[i]=='W': W[i]=1
    else: E[i]=1

for j in range(1, n):
    W[j] += W[j-1]
    E[j] += E[j-1]
    
for k in range(n):
    sum = W[k-1] + E[n-1] - E[k] 
    res = min(res, sum)

print(res)
