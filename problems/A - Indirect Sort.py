t = int(input())
for test_case in range(t):
    n = int(input())
    int_list = list(map(int, input().split()))
    if int_list[0] == 1:
        print("YES")
    else:
        print("NO")