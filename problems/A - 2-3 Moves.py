t = int(input())
for test_case in range(t):
    inp_ = int(input())
    if inp_ == 1:
        print(2)
    elif inp_ % 3 == 0:
        print(inp_ // 3)
    elif inp_ % 2 == 0:
        print(inp_ // 3 + 1)
    elif inp_ % 3 == 1:
        print(inp_ // 3 + 1)
    elif inp_ % 3 == 2:
        print(inp_ // 3 + 1)