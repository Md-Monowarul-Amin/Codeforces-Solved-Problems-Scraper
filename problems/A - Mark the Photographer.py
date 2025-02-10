t = int(input())
for test_case in range(t):
    n, x = map(int, input().split())
    int_list = list(map(int, input().split()))
    first = []
    last = []
    int_list.sort()
    for i in range(n):
        first.append(int_list[i])
    for j in range(n, 2 * n):
        last.append(int_list[j])
    ok = 1
    for i in range(n):
        if (first[i] + x) > (last[i]):
            ok = 0
            break
    if ok:
        print("YES")
    else:
        print("NO")
  