import math
 t = int(input())
for test_case in range(t):
    n = int(input())
    if n == 3 or n == 1:
        print(-1)
    else:
        out_list = []
        if n % 2 == 0:
            for i in range(n):
                out_list.append(n-i)
        else:
            for i in range(n//2):
                out_list.append(n-i)
            for i in range(1, n//2+2):
                out_list.append(i)
         for i in out_list:
            print(i, end=" ")
        print()