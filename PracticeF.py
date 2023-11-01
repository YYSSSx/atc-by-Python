n, a, b = map(int, input().split())
res = 0

for i in range(1, n+1):
    sum = 0
    num = i
    for _ in range(5):
        sum += num%10
        num //= 10
    if sum >= a and sum <= b:
        res += i

print(res)