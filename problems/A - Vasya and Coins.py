t = int(input())
for test_case in range(t):
    a, b = map(int, input().split())
    ans = 0
    if a == 0:
        ans = 0
    else:
        ans = a * 1 + b * 2
    print(ans + 1)