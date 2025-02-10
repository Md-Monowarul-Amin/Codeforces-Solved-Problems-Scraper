t = int(input())
for test_case in range(t):
    n = int(input())
    curr_ind = [0, 0]
    move = 0
    highest_x = -110
    lowest_x = 110
    highest_y = -110
    lowest_y = 110
     for inp_ in range(n):
        next_ind = list(map(int, input().split()))
        if next_ind[0] > highest_x:
            highest_x = next_ind[0]
        if next_ind[0] < lowest_x:
            lowest_x = next_ind[0]
        if next_ind[1] > highest_y:
            highest_y = next_ind[1]
        if next_ind[1] < lowest_y:
            lowest_y = next_ind[1]
     if highest_x > 0 and lowest_x > 0:
        move += lowest_x
    elif highest_x < 0 and lowest_x < 0:
        move += highest_x * (-1)
    if highest_y > 0 and lowest_y > 0:
        move += lowest_y
    elif highest_y < 0 and lowest_y < 0:
        move += highest_y * (-1)
     move += (abs(highest_x - lowest_x) + abs(highest_y - lowest_y))
    print(2 * move)
 