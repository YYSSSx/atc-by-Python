a, b = map(int, input().split())

cnt = 0

while a != b:
    times = 0
    if a > b:
        times = a/b
        a = a%b
    else:
        times = b/a
        b = b%a
        
    
    cnt += times

print(cnt)