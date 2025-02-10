t = int(input())
for test_case in range(t):
    str_ = input()
    if (str_[0] == "y" or str_[0] == "Y") and (str_[1] == "e" or str_[1] == "E") and (str_[2] == "s" or str_[2] == "S"):
        print("YES")
    else:
        print("NO")