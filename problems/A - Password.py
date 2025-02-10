def factorial(n):
    ans = 1
    while n >= 1:
        ans = ans * n
        n -= 1
    return ans
  t = int(input())
for test_case in range(t):
    n = int(input())
    int_list = list(map(int, input().split()))
     a = factorial(10 - n)
    b = factorial(10 - n - 2)
    c = factorial(2)
    print(int((a / (b * c)) * 6))
 