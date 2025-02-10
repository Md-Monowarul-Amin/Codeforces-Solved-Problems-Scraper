t = int(input())
for test_case in range(t):
    l, r, a = map(int, input().split())
    multi = r // a
    x = multi * a - 1
    if x < l:
        x = r
    print(max((x//a + x % a), (r//a + r % a)))
 