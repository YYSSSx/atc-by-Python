N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
def binary_search(arr, value):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] <= value:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result

res = 0
for i in range(N):
    a = binary_search(A, A[i]+M-1)
    cnt = a-i+1
    res = max(res, cnt)

print(res)
