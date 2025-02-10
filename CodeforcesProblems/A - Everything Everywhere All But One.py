t = int(input())
for test_case in range(t):
    n = int(input())
    int_list = list(map(int, input().split()))
    sum_int = sum(int_list)
    ok = 0
    for i in range(n):
        num = int_list[i]
        mean = (sum_int - num) / (n-1)
        if mean == num:
            ok = 1
            break
        else:
            continue
    if ok:
        print("YES")
    else:
        print("NO")