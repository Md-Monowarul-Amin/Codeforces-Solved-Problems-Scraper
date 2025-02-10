t = int(input())
for test_case in range(t):
    n, m = map(int, input().split())
    a = input()
    b = input()
    j = n-1
    ok = 1
    if n > m:
        for i in range(m-1, 0, -1):
            if b[i] == a[j]:
                j -= 1
                continue
            else:
                ok = 0
                break
        if ok:
            b_first = b[0]
            found = 0
            for i in range(n-m+1):
                if a[i] == b_first:
                    found = 1
                    break
            if found:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    elif n == m:
        do = 1
        for i in range(n):
            if a[i] != b[i]:
                do = 0
                break
        if do:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")