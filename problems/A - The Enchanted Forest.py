t = int(input())
for test_case in range(t):
    n, k = map(int, input().split())
    int_list = list(map(int, input().split()))
    if k == 1:
        ans = max(int_list)
        print(ans)
    elif k < n:
        i = 0
        j = k-1
        summation_old = 0
        for p in range(k):
            summation_old += int_list[p]
        summation_new = summation_old
        # print(summation_old)
        while (j+1) < n:
            j += 1
            summation_new = summation_new - int_list[i] + int_list[j]
            summation_old = max(summation_old, summation_new)
            # print(summation_old, i, j)
            i += 1
         print(summation_old + (k * (k-1)) // 2)
     else:
        summation = sum(int_list)
        summation += (n * (n-1)) // 2
        summation += (k-n) * n
        print(summation)