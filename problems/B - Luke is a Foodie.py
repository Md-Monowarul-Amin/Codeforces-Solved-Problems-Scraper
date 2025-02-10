def inside(range_list, curr_list):
    if (range_list[1] >= curr_list[1] >= range_list[0]) or (range_list[1] >= curr_list[0] >= range_list[0]):
        return True
    else:
        return False
  t = int(input())
for test_Case in range(t):
    n, x = map(int, input().split())
    int_list = list(map(int, input().split()))
    range_list = []
    for i in range(n):
        sm = int_list[i] - x
        bg = x + int_list[i]
        range_list.append([sm, bg])
    # print(range_list)
    cnt = 0
    curr_list = range_list[0]
    for i in range(n):
        if inside(range_list[i], curr_list):
            curr_list[0] = max(range_list[i][0], curr_list[0])
            curr_list[1] = min(range_list[i][1], curr_list[1])
            continue
        else:
            cnt += 1
            curr_list = range_list[i]
    print(cnt)
   