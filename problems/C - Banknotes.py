t = int(input())
for test_case in range(t):
    n, k = map(int, input().split())
    deno_list = list(map(int, input().split()))
    k = k + 1
    num_list = []
    for i in range(n-1):
        num_list.append(min(k - sum(num_list), 10 ** (deno_list[i+1] - deno_list[i])-1))
        # print(sum(num_list))
    num_list.append(k - sum(num_list))
     s = 0
    for i in range(n):
        s += num_list[i] * (10 ** deno_list[i])
    print(s)
 