t = int(input())
for test_case in range(t):
    n, m = map(int, input().split())
    word_list = []
    word_int_list = []
    for word in range(n):
        str_ = input()
        word_list.append(str_)
     for i in range(n):
        word_int_list.append([])
        for char in word_list[i]:
            word_char = ord(char)
            word_int_list[i].append(word_char)
     min_diff = 999999999999
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            else:
                diff = 0
                for k in range(m):
                    diff += abs(word_int_list[i][k] - word_int_list[j][k])
                if diff < min_diff:
                    min_diff = diff
     print(min_diff)
 