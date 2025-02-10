t = int(input())
for test_case in range(t):
    n = int(input())
    pos_int = int(input())
    if len(str((10 ** n - 1) - pos_int)) < n:
        pal_int = ""
        for i in range(n+1):
            pal_int += "1"
        pal_int = int(pal_int)
        print(pal_int - pos_int)
    else:
        print(10 ** n - 1 - pos_int)