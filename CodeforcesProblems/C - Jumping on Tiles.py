t = int(input())
for test_case in range(t):
    str_ = input()
    d = dict()
    cost = abs(ord(str_[len(str_)-1]) - ord(str_[0]))
    out_list = []
    str_num_list = []
    for i in range(len(str_)):
        temp_num = ord(str_[i]) - 96
        str_num_list.append(temp_num)
        if temp_num not in d:
            d[temp_num] = [i + 1]
        else:
            d[temp_num].append(i+1)
    str_num_list.sort()
    start = -1
    end = -1
     if ord(str_[0]) >= ord(str_[-1]):
        # print("a")
        init_index = ord(str_[0]) - 96
        end_index = ord(str_[-1]) - 96
        # print(init_index, end_index)
        for i in range(len(str_)-1, -1, -1):
            # print("ok")
            if str_num_list[i] == init_index:
                 start = i
                break
        for i in range(len(str_)):
            if str_num_list[i] == end_index:
                end = i
                break
     elif ord(str_[0]) < ord(str_[-1]):
        init_index = ord(str_[0]) - 96
        end_index = ord(str_[-1]) - 96
        for i in range(len(str_)-1, -1, -1):
            if str_num_list[i] == end_index:
                end = i
                break
        for i in range(len(str_)):
            if str_num_list[i] == init_index:
                start = i
                break
     if start > end:
        i = start
        while i >= end:
            # print(d[str_num_list[i]])
            for j in range(len(d[str_num_list[i]])):
                out_list.append(d[str_num_list[i]][j])
            i -= len(d[str_num_list[i]])
    else:
        i = start
        while i <= end:
            for j in range(len(d[str_num_list[i]])):
                out_list.append(d[str_num_list[i]][j])
            i += len(d[str_num_list[i]])
     # print(out_list)
    print(cost, len(out_list))
    for i in range(len(out_list)):
        print(out_list[i], end=" ")
    print()
    # print(d)
    # print(start, end)
    # print(str_num_list)
    # print(d)
  