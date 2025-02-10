t = int(input())
for test_case in range(t):
    n = int(input())
    line_1 = str(input())
    line_2 = str(input())
    ok = 1
    for i in range(n):
        if line_1[i] == line_2[i]:
            pass
        else:
            if (line_1[i] == "G" and line_2[i] == "B") or (line_1[i] == "B" and line_2[i] == "G"):
                pass
            else:
                ok = 0
                break
    if ok:
        print("YES")
    else:
        print("NO")
 