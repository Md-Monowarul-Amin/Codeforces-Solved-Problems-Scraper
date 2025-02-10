t = int(input())
for test_case in range(t):
    n = int(input())
    int_list = list(map(int, input().split()))
    int_list.sort()
    red = int_list[-1]
    red_index = -1
    blue_index = 1
    blue = int_list[0] + int_list[1]
    ok = 0
    if n % 2 == 0:
        barrier = n // 2 - 2
    else:
        barrier = n // 2 - 1
    if red > blue:
        ok = 1
        print("YES")
    else:
        for i in range(barrier):
            red_index -= 1
            blue_index += 1
            red += int_list[red_index]
            blue += int_list[blue_index]
            if red > blue:
                ok = 1
                break
            else:
                continue
        if ok == 1:
            print("YES")
        else:
            print("NO")
  