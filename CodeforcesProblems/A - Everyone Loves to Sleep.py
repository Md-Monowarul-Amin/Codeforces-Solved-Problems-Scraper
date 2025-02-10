t = int(input())
for test_case in range(t):
    n, V_H, V_M = map(int, input().split())
    sleeping_minute = V_H * 60 + V_M
    timing_list = []
    for time in range(n):
        A_h, A_m = (map(int, input().split()))
        minute = A_h * 60 + A_m
        timing_list.append(minute)
     ans_min = 24 * 60 - 1
    for i in range(n):
        if timing_list[i] >= sleeping_minute:
            ans_min = min(timing_list[i] - sleeping_minute, ans_min)
        else:
            ans_min = min(ans_min, 24 * 60 - (sleeping_minute - timing_list[i]))
    print(ans_min // 60, ans_min % 60)