t = int(input())
for test_case in range(t):
    n, m, s_x, s_y, d = map(int, input().split())
    if ((s_x + d) >= n and (s_y + d) >= m) or ((s_x - d) <= 1 and (s_y - d) <= 1):
        print(-1)
    elif ((s_x + d) >= n) and ((s_x - d) <= 1):
        print(-1)
     elif ((s_y + d) >= m) and ((s_y - d) <= 1):
        print(-1)
     else:
        print(n-1 + m - 1)