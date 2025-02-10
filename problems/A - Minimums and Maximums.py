t = int(input())
for test_case in range(t):
    l_1, r_1, l_2, r_2 = map(int, input().split())
    if l_1 <= l_2 <= r_1:
        print(l_2)
    elif r_2 >= l_1 >= l_2:
        print(l_1)
    else:
        print(l_1 + l_2)