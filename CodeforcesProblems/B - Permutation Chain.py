t = int(input())
for test_case in range(t):
    n = int(input())
    print(n)
    int_list = []
    for i in range(1, n+1):
        int_list.append(i)
    for out in int_list:
        print(out, end=" ")
    print()
    for i in range(1, n):
        swap = int_list[0]
        int_list[0] = int_list[i]
        int_list[i] = swap
        for out in int_list:
            print(out, end=" ")
        print()