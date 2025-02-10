t = int(input())
for test_case in range(t):
    n = int(input())
    d = dict()
    list_2d = []
    # out_list = []
    for i in range(3):
        list_ = list(map(str, input().split()))
        for word in list_:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
         list_2d.append(list_)
     # print(d)
    # print(list_2d)
    out_list = [0, 0, 0]
    for i in range(3):
        for j in range(n):
            if d[list_2d[i][j]] == 1:
                out_list[i] += 3
            elif d[list_2d[i][j]] == 2:
                out_list[i] += 1
            elif d[list_2d[i][j]] == 3:
                out_list[i] += 0
     for num in out_list:
        print(num, end=" ")
    print()