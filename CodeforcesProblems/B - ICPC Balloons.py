t = int(input())
for test_case in range(t):
    n = int(input())
    str_ = input()
    d = dict()
    for char in str_:
        if char in d:
            d[char] += 1
        else:
            d[char] = 2
    total = 0
    for i in d:
        total += d[i]
    print(total)
 