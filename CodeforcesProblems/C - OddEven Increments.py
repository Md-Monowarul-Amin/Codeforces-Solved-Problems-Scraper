def possible(list_, i, parity):
    if i+2 > len(list_)-1:
        return 1
    if parity == (list_[i+2] % 2):
        return possible(list_, i+2, parity)
    return 0
  t = int(input())
for test_case in range(t):
    n = int(input())
    int_list = list(map(int, input().split()))
    odd_ind_p = possible(int_list, 0, int_list[0] % 2)
    even_ind_p = possible(int_list, 1, int_list[1] % 2)
    # print(odd_ind_p, even_ind_p, int_list[0] % 2, int_list[1] % 2)
    if odd_ind_p and even_ind_p:
        print("YES")
    else:
        print("NO")