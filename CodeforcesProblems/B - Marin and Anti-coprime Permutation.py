import math
 t = int(input())
for test_case in range(t):
    n = int(input())
    if n % 2 != 0:
        print(0)
    else:
        print((math.factorial(n//2) ** 2) % 998244353)