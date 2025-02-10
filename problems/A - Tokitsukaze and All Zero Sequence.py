t = int(input())
for test_case in range(t):
    n = int(input())
    int_list = list(map(int, input().split()))
    # print(int_list)
    zero_count = 0
    common = 0
    for i in range(n):
        num = int_list[i]
        if common == 0:
            for j in range(n):
                if i == j:
                    continue
                else:
                    if int_list[j] == num:
                        common = 1
                        break
        else:
            break
    for i in range(n):
        if int_list[i] == 0:
            common = 1
            zero_count += 1
     ans = n + 1 - common - zero_count
    print(ans)
  