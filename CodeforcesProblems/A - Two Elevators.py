t = int(input())
for test_case in range(t):
    a, b, c = map(int, input().split())
    one = a - 1
    two = abs(b - c) + (c - 1)
    if one > two:
        print(2)
    elif two > one:
        print(1)
    else:
        print(3)
 