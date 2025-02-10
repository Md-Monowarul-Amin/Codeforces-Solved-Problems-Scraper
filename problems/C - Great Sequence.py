t = int(input())
for test_case in range(t):
    n, x = map(int, input().split())
    int_list = list(map(int, input().split()))
    int_list.sort()
    int_list_len = n
    d = dict()
    i = 0
    while i < n:
        num = int_list[i]
        d[num] = 1
        cnt = 1
        for j in range(i+1, n):
            if int_list[j] == num:
                d[num] += 1
                cnt += 1
            else:
                break
        # print(i)
        i = i + cnt
         if i == n:
            break
    # print(d)
     count = n
    for k in range(n):
        num = int_list[k]
        if d[num] > 0:
            num_2 = num * x
            if num_2 in d:
                if d[num_2] > 0:
                    d[num_2] -= 1
                    d[num] -= 1
                    count -= 2
    print(count)
 