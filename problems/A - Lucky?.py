t = int(input())
for test_case in range(t):
    num = input()
    pre = int(num[0]) + int(num[1]) + int(num[2])
    post = int(num[3]) + int(num[4]) + int(num[5])
    if post == pre:
        print("YES")
    else:
        print("NO")
 