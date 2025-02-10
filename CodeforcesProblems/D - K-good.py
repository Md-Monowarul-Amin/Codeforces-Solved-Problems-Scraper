t = int(input())
for test_case in range(t):
    n = int(input())
    two_n = 2 * n
    k = two_n
    for i in range(n):
        if k % 2 == 0:
            k = k // 2
        else:
            break
    if k == 1:
        print(-1)
    else:
        print(int(min(k, (n*2) // k)))
 