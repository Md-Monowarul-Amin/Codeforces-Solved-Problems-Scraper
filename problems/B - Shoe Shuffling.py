t = int(input())
for test_case in range(t):
    n = int(input())
    shoe_size_list = list(map(int, input().split()))
    size_dict = dict()
    cancel = 0
    for i in range(n):
        if shoe_size_list[i] in size_dict:
            size_dict[shoe_size_list[i]][0] += 1
            size_dict[shoe_size_list[i]].append(i+1)
            if size_dict[shoe_size_list[i]][0] == 2:
                cancel -= 1
        else:
            size_dict[shoe_size_list[i]] = [1, i+1]
            cancel += 1
    if cancel:
        print(-1)
    else:
        out_list = [-1] * n
        # print(out_list)
        # print(size_dict)
        for i in size_dict:
            for j in range(size_dict[i][0]-1):
                out_list[size_dict[i][j+1]-1] = size_dict[i][j+2]
             out_list[size_dict[i][-1]-1] = size_dict[i][1]
         for num in out_list:
            print(num, end=" ")
        print()
   