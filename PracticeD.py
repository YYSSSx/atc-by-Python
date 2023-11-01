n = int(input())
a = list(map(int, input().split()))

res = 0

while True:
    even = True
    for i in range(n):
        if a[i]%2 == 1:
            even = False
        else:
            a[i] /=2
    if even == False:
        break
    else:
        res += 1

print(res)
