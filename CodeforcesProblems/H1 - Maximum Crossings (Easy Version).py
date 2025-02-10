t = int(input())
for test_case in range(t):
    n = int(input())
    cross_list = list(map(int, input().split()))
    cross = 0
    for i in range(n):
        base_line = cross_list[i]
        for j in range(i+1, n):
            cross_check = cross_list[j]
            if cross_check <= base_line:
                cross += 1
    print(cross)