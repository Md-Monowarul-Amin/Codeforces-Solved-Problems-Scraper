t = int(input())
for test_case in range(t):
    a = input()
    c = input()
     count = 0
    color_list = []
    # print(ord(a[0]), ord(a[1]), ord(c[0]), ord(c[1]))
    # print(a, c)
    for i in range(27):
        color_list.append(0)
    # print(ord(a[0])-97)
    if color_list[ord(a[0])-97] != 0:
        # print(ord(a[0])-97)
        pass
    else:
        color_list[ord(a[0])-97] = 1
        count += 1
     if color_list[ord(a[1])-97] != 0:
        pass
    else:
        color_list[ord(a[1])-97] = 1
        count += 1
     if color_list[ord(c[0])-97] != 0:
        pass
    else:
        color_list[ord(c[0])-97] = 1
        count += 1
     if color_list[ord(c[1])-97] != 0:
        pass
    else:
        color_list[ord(c[1])-97] = 1
        count += 1
     print(count-1)
    # print(a, c)
    # print(count-1)
     