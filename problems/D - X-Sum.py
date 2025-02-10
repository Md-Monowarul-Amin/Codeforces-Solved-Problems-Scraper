def left_up(i, j, list_2D, n, m):
    sum = 0
    while i >= 0 and j >= 0:
        sum += list_2D[i][j]
        i -= 1
        j -= 1
    return sum
  def right_up(i, j, list_2D, n, m):
    sum = 0
    while i >= 0 and j <= m-1:
        sum += list_2D[i][j]
        i -= 1
        j += 1
    return sum
  def left_down(i, j, list_2D, n, m):
    sum = 0
    while i <= n-1 and j >= 0:
        sum += list_2D[i][j]
        i += 1
        j -= 1
    return sum
  def right_down(i, j, list_2D, n, m):
    sum = 0
    while i <= n-1 and j <= m-1:
        sum += list_2D[i][j]
        i += 1
        j += 1
    return sum
  t = int(input())
for test_case in range(t):
    n, m = map(int, input().split())
    int_list_2D = []
    for i in range(n):
        row = list(map(int, input().split()))
        int_list_2D.append(row)
    ans = 0
    for i in range(n):
        for j in range(m):
            left_up_sum = left_up(i, j, int_list_2D, n, m)
            left_down_sum = left_down(i, j, int_list_2D, n, m)
            right_up_sum = right_up(i, j, int_list_2D, n, m)
            right_down_sum = right_down(i, j, int_list_2D, n, m)
            total = left_down_sum + left_up_sum + right_up_sum + right_down_sum - 3 * int_list_2D[i][j]
            if total > ans:
                ans = total
    print(ans)