t = int(input())
for test_case in range(t):
    s = int(input())
    if s <= 9:
        print(s)
    else:
        str_ = "9"
        s = s - 9
        char = 8
        while s > 0:
            if s > char:
                s -= char
                str_ = str(char) + str_
                char = char - 1
            else:
                str_ = str(s) + str_
                break
        print(str_)