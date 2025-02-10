import math
 t = int(input())
for test_case in range(t):
    n, k = map(int, input().split())
    int_list = list(map(int, input().split()))
    total = 0
    if k == 1:
        total = math.ceil((n-2) / 2)
    else:
        for i in range(1, n-1):
            if int_list[i] > (int_list[i-1] + int_list[i+1]):
                total += 1
     print(total)