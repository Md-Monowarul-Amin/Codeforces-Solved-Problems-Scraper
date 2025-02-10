t = int(input())
for test_case in range(t):
    n = int(input())
    int_list = list(map(int, input().split()))
    out_list = []
    out = n
    ok = 0
    minus = 0
    if out % 2 != 0:
        ok = "odd"
    else:
        ok = "even"
    for i in range((10 ** 4)+10):
        out_list.append(0)
    for i in int_list:
        if out_list[i] == 1:
            out -= 1
            minus = 1
        else:
            out_list[i] = 1
    if minus:
        if ok == "odd" and out % 2 == 0:
            out -= 1
        elif ok == "even" and out % 2 != 0:
            out -= 1
     print(out)