t = int(input())
for test_case in range(t):
    n = int(input())
    int_list = list(map(int, input().split()))
    prob = 0
    ans = "YES"
    for i in range(n-1):
        if int_list[i+1] > int_list[i]:
            if not prob:
                continue
            else:
                ans = "NO"
                break
        elif int_list[i+1] < int_list[i]:
            prob = 1
        else:
            continue
     print(ans)