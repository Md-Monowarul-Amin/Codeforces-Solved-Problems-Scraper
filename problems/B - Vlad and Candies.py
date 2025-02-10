t = int(input())
for test_case in range(t):
    n = int(input())
    int_list = list(map(int, input().split()))
    int_list_max = max(int_list)
    max_index = int_list.index(int_list_max)
    ok = 0
    if n == 1:
        if int_list[0] == 1:
            ok = 1
    else:
        for i in range(n):
            if i == max_index:
                continue
            else:
                if int_list[i] == int_list_max-1 or int_list[i] == int_list_max:
                    ok = 1
                    break
    if ok:
        print("YES")
    else:
        print("NO")