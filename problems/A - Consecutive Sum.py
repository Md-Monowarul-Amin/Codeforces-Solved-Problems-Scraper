t = int(input())
for test_case in range(t):
    n, k = map(int, input().split())
    int_list = list(map(int, input().split()))
    d = dict()
    for i in range(k):
        d[i] = []
    for i in range(n):
        mod_value = i % k
        d[mod_value].append(int_list[i])
     total_sum = 0
    for i in range(k):
        total_sum += max(d[i])
     print(total_sum)
 