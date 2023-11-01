X, Y = map(int, input().split())

d = Y-X
if 0<d<=2 or 0>d>=-3:
    print('Yes')
else:
    print('No')