t = int(input())
for test_case in range(t):
    n = int(input())
    health_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
     total = sum(health_list)
    add = sum(b_list) - max(b_list)
    ans = total + add
     print(ans)
 