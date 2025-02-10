t = int(input())
for test_case in range(t):
    n = int(input())
    given_name = str(input())
    if len(given_name) == 5:
        if "T" in given_name and "i" in given_name and "m" in given_name and "u" in given_name and "r" in given_name:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
     