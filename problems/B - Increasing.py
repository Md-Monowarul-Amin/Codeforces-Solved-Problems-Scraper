t = int(input())
for test_case in range(t):
    n = int(input())
    int_list = list(map(int, input().split()))
    d = dict()
    ok = 1
    for i in range(len(int_list)):
        if int_list[i] not in d:
            d[int_list[i]] = 1
        else:
            ok = 0
            break
    if ok:
        print("YES")
    else:
        print("NO")