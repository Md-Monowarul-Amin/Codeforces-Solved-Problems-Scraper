t = int(input())
for test_case in range(t):
    n = int(input())
    int_list = list(map(int, input().split()))
    if len(int_list) > 1:
        sorted_ = 1
        for i in range(n-1):
            if int_list[i] < int_list[i+1]:
                pass
            else:
                sorted_ = 0
                break
         if not sorted_:
            out_list = []
            if (int_list[0] + int_list[n-1]) % 2 == 0:
                int_list[0] = int_list[n-1]
            else:
                int_list[n-1] = int_list[0]
            out_list.append([1, n])
             for i in range(1, n-1):
                if (int_list[i] + int_list[0]) % 2 != 0:
                    out_list.append([1, i+1])
                else:
                    out_list.append([i+1, n])
             print(len(out_list))
            for i in range(len(out_list)):
                # print(int_list)
                print(out_list[i][0], out_list[i][1])
                # print()
        else:
            print(0)
    else:
        print(0)
 