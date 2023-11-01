n = int(input())
d = []
for _ in range(n):
    d.append(int(input()))

res = 1

d.sort(reverse=True)

for j in range(1, n):
    if d[j] < d[j-1]:
        res += 1

print(res)