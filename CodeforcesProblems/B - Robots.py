t = int(input())
for test_case in range(t):
    n, m = map(int, input().split())
    str_list_2D = []
    for row in range(n):
        str_list = input()
        str_list_2D.append(str_list)
    nearest_row = "00"
    nearest_col = "00"
    ok_row = 0
    for i in range(n):
        if ok_row == 0:
            for j in range(m):
                if str_list_2D[i][j] == "R":
                    nearest_row = str(i) + str(j)
                    ok_row = 1
                    break
     ok_col = 0
    for i in range(m):
        if ok_col == 0:
            for j in range(n):
                if str_list_2D[j][i] == "R":
                    # print(j, i)
                    nearest_col = str(j) + str(i)
                    ok_col = 1
                    break
    """d = nearest_row
    nearest_row = nearest_col
    nearest_col = d"""
    if int(nearest_row[1]) <= int(nearest_col[1]) and nearest_col[0] <= nearest_row[0]:
        print("YES")
    else:
        print("NO")