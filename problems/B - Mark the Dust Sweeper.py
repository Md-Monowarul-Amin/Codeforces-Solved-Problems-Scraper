t = int(input())
for test_case in range(t):
    n = int(input())
    int_list = list(map(int, input().split()))
    zero_count = 0
    for i in range(n-1):
        if int_list[i] == 0:
            zero_count += 1
    pre_zero = 0
    for i in range(n-1):
        if int_list[i] != 0:
            break
        else:
            pre_zero += 1
    cnt = 0
    for i in range(n-1):
        cnt += int_list[i]
    print(cnt + zero_count - pre_zero)
    # print(zero_count, pre_zero)
 