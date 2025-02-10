t = int(input())
for test_case in range(t):
    n, s = map(int, input().split())
    count = s // (n ** 2)
    print(count)