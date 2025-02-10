t = int(input())
for test_case in range(t):
    n = int(input())
    string = input()
    odd_ind_list = []
    pirt_list = []
    count = 0
    for i in range(n-1):
        if string[i] == string[i+1]:
            count += 1
        else:
            count += 1
            pirt_list.append(count)
            count = 0
    pirt_list.append(count+1)
    # print(pirt_list)
    for i in range(len(pirt_list)):
        if pirt_list[i] % 2 != 0:
            odd_ind_list.append(i)
    ans = 0
    # print(odd_ind_list)
    for i in range(0, len(odd_ind_list), 2):
        ans += odd_ind_list[i+1] - odd_ind_list[i]
    print(ans)