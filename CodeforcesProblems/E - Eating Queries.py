t = int(input())
for test_case in range(t):
    n, q = map(int, input().split())
    int_list = list(map(int, input().split()))
    int_list.sort()
    int_list.reverse()
    int_list_pref_sum = [int_list[0]]
    pref_sum = int_list[0]
    for i in range(1, n):
        pref_sum += int_list[i]
        int_list_pref_sum.append(pref_sum)
     for query in range(q):
        level = int(input())
        # print(int_list)
        # print(int_list_pref_sum)
        l = 0
        r = n - 1
        ans = 10 ** 9
        while l <= r:
            mid = l + (r - l) // 2
            if int_list_pref_sum[mid] > level:
                ans = min(ans, mid)
                # print(ans)
                r = mid - 1
            elif int_list_pref_sum[mid] == level:
                ans = mid
                # print(mid)
                break
            else:
                l = mid + 1
        if ans == 10 ** 9:
            ans = -2
        print(ans + 1)