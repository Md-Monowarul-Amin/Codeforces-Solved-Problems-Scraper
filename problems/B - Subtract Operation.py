t = int(input())
for test_case in range(t):
    n, k = map(int, input().split())
    int_list = list(map(int, input().split()))
    int_list.sort()
    ok = 0
    for i in range(n):
        index_init = int_list[i]
        left = i
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if (int_list[mid] - index_init) == k:
                ok = 1
                break
            elif (int_list[mid] - index_init) > k:
                right = mid - 1
            elif (int_list[mid] - index_init) < k:
                left = mid + 1
         if ok == 1:
            break
        else:
            continue
     if ok:
        print("YES")
    else:
        print("NO")
  