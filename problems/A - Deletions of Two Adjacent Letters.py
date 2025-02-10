t = int(input())
for test_case in range(t):
    string = input()
    c = input()
    ok = 0
    for i in range(len(string)):
        if string[i] == c:
            if i % 2 == 0:
                ok = 1
                break
    if ok:
        print("YES")
    else:
        print("NO")