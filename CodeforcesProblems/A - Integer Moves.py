import math
 t = int(input())
 for test_case in range(t):
    x, y = map(int, input().split())
    diff = ((0-x) ** 2 + (0 - y) ** 2) ** .5
    diff_ceil = math.ceil(diff)
    if x == 0 and y == 0:
        print(0)
    elif diff == diff_ceil:
        print(1)
    else:
        print(2)