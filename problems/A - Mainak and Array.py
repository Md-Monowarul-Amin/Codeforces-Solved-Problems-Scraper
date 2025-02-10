t = int(input())
for test_case in range(t):
    n = int(input())
    int_list = list(map(int, input().split()))
    max_num = max(int_list)
    min_num = min(int_list)
     exception = 0
     ans = -1
    for i in range(n-1):
        if int_list[i] == max_num and int_list[i+1] == min_num:
            exception = 1
    if abs(min_num-int_list[n-1]) > abs(max_num - int_list[0]):
        ans = abs(min_num-int_list[n-1])
    else:
        ans = abs(max_num - int_list[0])
     maximum_consecutive_distance = -1
    for i in range(n-1):
        if int_list[i] - int_list[i+1] > maximum_consecutive_distance:
            maximum_consecutive_distance = int_list[i] - int_list[i+1]
     if maximum_consecutive_distance > ans:
        ans = maximum_consecutive_distance
    print(ans)