t = int(input())
for test_case in range(t):
    n, c = map(int, input().split())
    int_list = list(map(int, input().split()))
    d = dict()
    for i in range(n):
        if int_list[i] not in d:
            d[int_list[i]] = 1
        else:
            d[int_list[i]] += 1
     # print(d)
    out = 0
    for i in d:
        if d[i] > c:
            out += c
        else:
            out += d[i]
     print(out)