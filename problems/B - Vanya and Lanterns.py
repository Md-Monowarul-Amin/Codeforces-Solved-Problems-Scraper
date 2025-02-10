n, l = map(int, input().split())
int_list = list(map(int, input().split()))
if n == 1:
    print(max(int_list[0] - 0, l - int_list[0]))
else:
    int_list.sort()
    diff_list = []
    init = int_list[0]
    max_diss = max(int_list[0], l - int_list[-1])
    # print(max_diss / 2)
     for i in range(1, n):
        diff_list.append(int_list[i] - int_list[i-1])
     l = 0
    r = n
    max_diss = max(max(diff_list) / 2, max_diss)
    print(max_diss)
  