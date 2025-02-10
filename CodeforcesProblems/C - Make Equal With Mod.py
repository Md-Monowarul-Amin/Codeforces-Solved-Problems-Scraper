from math import gcd
t = input()
t = int(t)
for test in range(t):
    n = int(input())
    int_list = list(map(int, input().split()))
    all_same = True
    one = int_list[0]
    for i in range(n):
        if int_list[i] != one:
            all_same = False
            break
        else:
            continue
    if all_same:
        print("YES")
    else:
         if 1 not in int_list:
            print("YES")
        else:
            ok = 1
            int_list.sort()
            for i in range(n-1):
                if int_list[i] + 1 == int_list[i+1]:
                    ok = 0
                    break
            if ok:
                print("YES")
            else:
                print("NO")