from itertools import combinations
 fact_list = [6]
  def ones(s):
    # print(s)
    return bin(s).count("1")
  for i in range(15):
    fact_list.append(fact_list[i] * (i+4))
 """for i in range(2, 48):
    fact_list.append(2 ** i)"""
 """fact_list.sort()"""
 # print(fact_list)
 t = int(input())
for test_case in range(t):
    n = int(input())
    ans = ones(n)
    l = 0
    r = 16
    initial_index = 0
    while l <= r:
        mid = l + (r - l) // 2
        if fact_list[mid] < n:
            initial_index = max(mid, initial_index)
            l = mid + 1
        elif fact_list[mid] > n:
            r = mid - 1
        else:
            initial_index = mid
            # print(initial_index)
            break
    f = 0
    f_cnt = 0
    terms = initial_index
     for i in range(initial_index+1):
        combined_list = list(combinations(fact_list, i+1))
        for each_combined in combined_list:
            each_sum = sum(each_combined)
            if each_sum <= n:
                ans = min(ans, len(each_combined) + ones(n - each_sum))
     # print(n)
    # ans = ans + ones(n)
    print(ans)
 