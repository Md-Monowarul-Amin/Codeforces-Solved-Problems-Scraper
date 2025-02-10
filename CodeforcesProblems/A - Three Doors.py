t = int(input())
for test_case in range(t):
    x = int(input())
    int_list = list(map(int, input().split()))
    num = x
    ok = 1
    for i in range(2):
        if int_list[num-1]:
            num = int_list[num-1]
            continue
        else:
            ok = 0
            break
    if ok:
        print("YES")
    else:
        print("NO")