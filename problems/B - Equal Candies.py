t = int(input())
for test_case in range(t):
    n = int(input())
    int_list = list(map(int, input().split()))
    min_num = min(int_list)
    total = 0
    for i in range(n):
        total = total + int_list[i] - min_num
    print(total)
 