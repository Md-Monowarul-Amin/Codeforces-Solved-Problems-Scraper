t = int(input())
for test_case in range(t):
    n = int(input())
    num = str(input())
    # print(num)
    out_str = ""
    i = len(num) - 1
    while i >= 0:
        if num[i] == "0":
            part_num = int(num[i-2] + num[i-1])
            # print(part_num)
            i -= 3
        else:
            part_num = int(num[i])
            i -= 1
        # print(part_num)
        out_str = chr(part_num + 97 - 1) + out_str
    print(out_str)