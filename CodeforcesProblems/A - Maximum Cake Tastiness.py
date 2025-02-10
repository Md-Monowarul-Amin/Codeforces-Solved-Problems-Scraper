t = int(input())
for test_case in range(t):
    n = int(input())
    int_list = list(map(int, input().split()))
    int_list.sort()
    int_list.reverse()
    print(int_list[0] + int_list[1])