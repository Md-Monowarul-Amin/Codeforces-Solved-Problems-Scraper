t = int(input())
for test_case in range(t):
    n, z = map(int, input().split())
    int_list = list(map(int, input().split()))
    maxim = 0
    for i in int_list:
        if (i | z) > maxim:
            maxim = i | z
    print(maxim)