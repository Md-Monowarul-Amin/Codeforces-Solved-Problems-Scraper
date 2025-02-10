t = int(input())
for test_case in range(t):
    n = int(input())
    int_list = list(map(int, input().split()))
    d = dict()
    prefix = 0
    # print(d[0])
    for i in range(n-1, -1, -1):
        if int_list[i] in d:
            prefix = i + 1
            break
        else:
            d[int_list[i]] = 1
    print(prefix)