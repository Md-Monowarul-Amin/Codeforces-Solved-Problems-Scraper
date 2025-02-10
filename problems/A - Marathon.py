t = int(input())
for test_case in range(t):
    int_list = list(map(int, input().split()))
    a = int_list[0]
    int_list.sort()
    pos = -1
    for i in range(4):
        if int_list[i] == a:
            pos = i + 1
            break
    print(4 - pos)
    