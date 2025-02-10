t = int(input())
for test_case in range(t):
    n = int(input())
    int_list = list(map(int, input().split()))
     max_value = 0
    max_index = -1
    min_value = 10 ** 9 + 100
    min_index = -1
     for i in range(n):
        if int_list[i] > max_value:
            max_value = int_list[i]
            max_index = i + 1
        if int_list[i] < min_value:
            min_value = int_list[i]
            min_index = i + 1
     print(min_index, max_index)
  