t = int(input())
for test_case in range(t):
    n, B, x, y = map(int, input().split())
    summation = 0
    int_list = [0]
    for i in range(n):
        if (int_list[i] + x) > B:
            int_list.append(int_list[i] - y)
        else:
            int_list.append(int_list[i] + x)
        summation += int_list[i+1]
    print(summation)