def bishop_pos_cnt(str_list_2D_, row_):
    prev_row = 0
    aft_row = 0
    for i in range(8):
        if str_list_2D_[row_-1][i] == "#":
            prev_row += 1
        if str_list_2D_[row_+1][i] == "#":
            aft_row += 1
    if prev_row == 2 and aft_row == 2:
        return True
    else:
        return False
  t = int(input())
for test_case in range(t):
    emp = input()
    str_list_2D = []
    for i in range(8):
        str_list = input()
        str_list_2D.append(str_list)
    # print(str_list_2D)
    for row in range(1, 7):
        cnt = 0
        for col in range(1, 7):
            if str_list_2D[row][col] == "#":
                cnt += 1
                # print(cnt)
         if cnt == 1:
            ok = bishop_pos_cnt(str_list_2D, row)
            if ok:
                r = row + 1
                c = 0
                for i in range(1, 7):
                    if str_list_2D[row][i] == "#":
                        c = i + 1
                        break
                print(r, c)
                break
            else:
                continue
        else:
            cnt = 0
   