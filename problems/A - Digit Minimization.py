t = int(input())
for test_case in range(t):
    num = input()
    small = 1000000000
    if len(num) == 2:
        small = num[1]
    else:
        for digit in num:
            if int(digit) < small:
                small = int(digit)
    print(small)
 