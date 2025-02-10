t = int(input())
for test_case in range(t):
    n = int(input())
    if n % 2 != 0:
        print(-1)
    else:
        print(n//2, n//2, 0)