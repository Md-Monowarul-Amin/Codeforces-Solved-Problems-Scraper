t = int(input())
for test_case in range(t):
    n = int(input())
    int_list = list(map(int, input().split()))
    out = 0
    for i in range(n):
        new_list = []
        for j in range(n):
            if i == j:
                continue
            else:
                new_list.append(int_list[j])
        xor = new_list[0]
        for k in range(1, n-1):
            xor = xor^int_list[k]
        if xor == int_list[i]:
            out = xor
            print(out)
            break
  