t = int(input())
for test_case in range(t):
    n, k = map(int, input().split())
    string_ = input()
    summation = 0
     one_count = 0
    for i in range(n-1):
        if string_[i] == "1":
            one_count += 1
            if i == 0:
                summation += 10
            else:
                summation += 11
    if string_[n-1] == "1":
        summation += 1
        one_count += 1
     if one_count > 1:
        first_1 = n
        last_1 = 0
        for i in reversed(range(n)):
            if string_[i] == "1":
                last_1 = i+1
                break
         if k >= n-last_1:
            if last_1 == n:
                pass
            else:
                summation -= 10
            k -= (n-last_1)
         for i in range(n):
            if string_[i] == "1":
                first_1 = i + 1
                break
         if k >= first_1 - 1:
            if first_1 == 1:
                pass
            else:
                summation -= 1
    elif one_count == 1:
         one_position = -1
        for i in range(n):
            if string_[i] == "1":
                one_position = i + 1
                break
        if one_position == n:
            summation = 1
        else:
            if n - one_position <= k:
                summation = 1
            elif one_position - 1 <= k:
                summation = 10
            else:
                summation = 11
     print(summation)