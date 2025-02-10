t = int(input())
for test_case in range(t):
    n, m = map(int, input().split())
    list_2D = []
    one_list = [[1,0],[0,1]]
    zero_list = [[0,1], [1,0]]
    for i in range(n):
        list_2D.append([])
     for i in range(0,n):
        for j in range(m // 2):
            if i % 4 == 0:
                if j % 2 == 0:
                    list_2D[i].append(one_list[0])
                else:
                    list_2D[i].append(one_list[1])
            elif i % 4 == 1:
                if j % 2 != 0:
                    list_2D[i].append(one_list[0])
                else:
                    list_2D[i].append(one_list[1])
            elif i % 4 == 2:
                if j % 2 == 0:
                    list_2D[i].append(one_list[1])
                else:
                    list_2D[i].append(one_list[0])
            elif i % 4 == 3:
                if j % 2 ==0:
                    list_2D[i].append(one_list[0])
                else:
                    list_2D[i].append(one_list[1])
     for i in range(n):
        for j in range(m // 2):
            for k in range(2):
                print(list_2D[i][j][k], end=" ")
        print()
    # print(list_2D)
  