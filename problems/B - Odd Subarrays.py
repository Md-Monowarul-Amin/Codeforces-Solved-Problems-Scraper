import math
  def decrease(list_int, i):
    if list_int[i+1] < list_int[i]:
        return True
    else:
        return False
  t = int(input())
for test_case in range(t):
    fluctuate = 0
    n = int(input())
    int_list = list(map(int, input().split()))
    i = 0
    while i < n-1:
        if decrease(int_list, i):
            fluctuate += 1
            i += 2
        else:
            i += 1
    print(fluctuate)
  