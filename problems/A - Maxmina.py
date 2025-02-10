t = int(input())
for  test_case in range(t):
    n, k = map(int,input().split())
    int_list  = list(map(int, input().split()))
    ok = 0
    for i in range(n):
        if int_list[i] == 1:
            ok = 1
            break
     if ok:
        print("YES")
    else:
        print("NO")