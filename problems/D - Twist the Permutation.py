def left_shift(list, shift_num):
    new_list = []
    for i in range(shift_num, len(list)):
        new_list.append(list[i])
    for i in range(shift_num):
        new_list.append(list[i])
    return new_list
  t = int(input())
for test_case in range(t):
    n = int(input())
    output_str = ""
    int_list = list(map(int, input().split()))
    len_list = n
     for i in range(n):
        int_index = int_list.index(len_list)
        # print(int_index)
        if int_index+1 == len_list:
            output_str = " 0" + output_str
            int_list.pop(len_list - 1)
        else:
            output_str = " "+str(int_index+1) + output_str
            int_list = left_shift(int_list, int_index+1)
            int_list.pop(len_list - 1)
         len_list -= 1
    print(output_str)