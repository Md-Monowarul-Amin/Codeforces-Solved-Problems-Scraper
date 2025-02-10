t = int(input())
for test_case in range(t):
    n = int(input())
    int_list = list(map(int, input().split()))
    highest_first = -1
    highest_first_ind = -1
    lowest_first = 10 ** 10
    lowest_first_ind = -1
     highest_second = -1
    highest_second_ind = -1
    lowest_second = 10 ** 10
    lowest_second_ind = -1
     # highest_first
    for i in range(n):
        if int_list[i] > highest_first:
            highest_first = int_list[i]
            highest_first_ind = i
     # highest_second
    for i in range(n):
        if int_list[i] > highest_second and i != highest_first_ind:
            highest_second = int_list[i]
            highest_second_ind = i
     # lowest_first
    for i in range(n):
        if int_list[i] < lowest_first:
            lowest_first = int_list[i]
            lowest_first_ind = i
     # lowest_second
    for i in range(n):
        if int_list[i] < lowest_second and i != lowest_first_ind:
            lowest_second = int_list[i]
            lowest_second_ind = i
     # print(highest_first, highest_second, lowest_first, lowest_second)
    print(highest_first + highest_second - lowest_first - lowest_second)