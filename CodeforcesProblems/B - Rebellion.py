t = int(input())
for test_case in range(t):
    n = int(input())
    int_list = list(map(int, input().split()))
     decrease_points = []
    first_one = -1
    last_zero = -1
    for i in range(n):
        if int_list[i] == 1:
            first_one = i
            break
     for i in range(n):
        if int_list[i] == 0:
            last_zero = i
     ans = 0
    if last_zero == -1 or first_one == -1:
        ans = 0
    else:
        finish = 0
        for i in range(first_one, n):
            if int_list[i] == 1:
                for j in range(last_zero, -1, -1):
                    if i >= j:
                        finish = 1
                        break
                    else:
                        if int_list[j] == 0:
                            ans += 1
                            int_list[j] = 1
                            last_zero = j
                            break
                if finish:
                    break
     print(ans)