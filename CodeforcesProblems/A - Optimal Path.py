t = int(input())
for test_case in range(t):
    n, m = map(int, input().split())
    r_1 = ((m+1) * m) // 2
    j_m = m * ((n * (n+1)) // 2) - m
    print(r_1 + j_m)
    