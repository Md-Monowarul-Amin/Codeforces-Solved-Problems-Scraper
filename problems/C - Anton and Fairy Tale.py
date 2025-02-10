import math
 n, m = map(int, input().split())
# print()
l = 0
r = 10 ** 18 + 1
out = -1
if m >= n:
    out = n
else:
    while l <= r:
        mid = l + (r-l) // 2
        # print(mid, l, r)
         d = mid
        # print((d + m + 1) * (d - m), 2 * (d - m - 1) * m)
        if (d+m+1) * (d - m) >= 0 and 2 * (d-m-1)*m >= 0:
            if (2 * n) == ((d+m+1) * (d - m) - 2 * (d-m-1)*m):
                out = mid
                # print("OK")
                break
            elif 2 * n < ((d+m+1) * (d - m)) - (2 * (d-m-1)*m):
                out = mid
                # print(out,  (d+m+1) * (d - m) , (2 * (d-m-1)*m))
                # print(((d+m+1) * (d - m)) - (2 * (d-m-1)*m))
                r = mid - 1
            else:
                l = mid + 1
        else:
            l = mid + 1
print(out)