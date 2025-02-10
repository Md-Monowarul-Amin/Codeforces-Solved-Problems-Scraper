t = int(input())
for test_case in range(t):
    n = int(input())
    int_list = [-1] * n
    # print(int_list)
    if n % 2 == 0:
        j = 0
        for i in range(n, 0, -1):
            int_list[j] = i
            j += 1
     else:
        int_list[0] = 1
        j = 1
        for i in range(n, 1, -1):
            int_list[j] = i
            j += 1
     for i in range(1, n):
        if int_list[i] % (i+1) == 0:
            if i+2 < n:
                swap = int_list[i+2]
                int_list[i+2] = int_list[i]
                int_list[i] = swap
            else:
                swap = int_list[i - 2]
                int_list[i - 2] = int_list[i]
                int_list[i] = swap
     for i in int_list:
        print(i, end=" ")
    print()
    