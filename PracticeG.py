n = int(input())
a = list(map(int, input().split()))

a.sort(reverse = True)

A = a[0::2]
B = a[1::2]

sumA = sum(A)
sumB = sum(B)
res = sumA - sumB

print(res)