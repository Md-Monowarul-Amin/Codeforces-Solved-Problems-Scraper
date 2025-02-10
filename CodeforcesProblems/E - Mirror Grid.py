import math
  def shrink(list_2d, a, b, c, d, rw):
    a[0] = rw
    a[1] = rw
    b[0] = rw
    b[1] = n - 1 - rw
    c[0] = n - 1 - rw
    c[1] = n - 1 - rw
    d[0] = n - 1 - rw
    d[1] = rw
    return a, b, c, d
  def rotate(a, b, c, d):
    a[1] = a[1] + 1
    b[0] = b[0] + 1
    c[1] = c[1] - 1
    d[0] = d[0] - 1
    return a, b, c, d
  def change(list_2D, a, b, c, d):
    one_count = 0
    zero_count = 0
    if list_2D[a[0]][a[1]] == 1:
        one_count += 1
    else:
        zero_count += 1
     if list_2D[b[0]][b[1]] == 1:
        one_count += 1
    else:
        zero_count += 1
     if list_2D[c[0]][c[1]] == 1:
        one_count += 1
    else:
        zero_count += 1
     if list_2D[d[0]][d[1]] == 1:
        one_count += 1
    else:
        zero_count += 1
     return min(one_count, zero_count)
  t = int(input())
for test_case in range(t):
    n = int(input())
    out = 0
    list_2D = []
    for i in range(n):
        r = []
        row = input()
        for i in row:
            r.append(int(i))
        list_2D.append(r)
    # print(list_2D)
    a = [0, 0]
    b = [0, n-1]
    c = [n-1, n-1]
    d = [n-1, 0]
    rw = 1
    for sq in range(n, 0, -2):
        # print(a, b, c, d, sq)
        # print(sq)
        out += change(list_2D, a, b, c, d)
        for rt in range(sq - 2):
            # print(rt)
            a, b, c, d = rotate(a, b, c, d)
            out += change(list_2D, a, b, c, d)
            # print(out)
            # print(a, b, c, d)
         a, b, c, d = shrink(list_2D, a, b, c, d, rw)
         rw += 1
    print(out)