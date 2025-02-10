t = int(input())
for test_case in range(t):
    n = int(input())
    int_list = list(map(int, input().split()))
    odd_cnt = 0
    even_cnt = 0
    for i in range(n):
        if int_list[i] % 2 == 0:
            even_cnt += 1
        else:
            odd_cnt += 1
    print(min(even_cnt, odd_cnt))
 