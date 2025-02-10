t = int(input())
for test_case in range(t):
    list_int = list(map(int, input().split()))
    list_int.sort()
    if list_int[0] + list_int[1] == list_int[2]:
        print("YES")
    else:
        print("NO")
 