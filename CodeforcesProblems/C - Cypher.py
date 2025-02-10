t = int(input())
for test_case in range(t):
    n = int(input())
    present_lock_state = list(map(int, input().split()))
    change_2D = []
    for i in range(n):
        change = list(map(str, input().split()))
        u_count = 0
        d_count = 0
        for j in change[1]:
            if j == "D":
                d_count += 1
            elif j == "U":
                u_count += 1
        present_lock_state[i] = (present_lock_state[i] + d_count - u_count) % 10
    for i in present_lock_state:
        print(i, end=" ")
    print()
  