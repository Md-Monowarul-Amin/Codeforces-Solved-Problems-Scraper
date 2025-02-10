"""def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    print(decimal)"""
  t = int(input())
for test_case in range(t):
    x = int(input())
    if x == 1:
        print(3)
    else:
        bin_x = bin(x).replace("0b", "")
        opp_bin = ""
        for i in reversed(bin_x):
            opp_bin += i
        # print(bin_x, opp_bin)
         out = 0
        for i in range(len(opp_bin)):
            if opp_bin[i] == "1":
                out = 2 ** i
                # print(out)
                break
        if out == x:
            out += 1
        print(out)
 