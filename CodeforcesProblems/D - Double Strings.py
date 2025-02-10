def split_a(str_, ind):
    a = ""
    for i in range(ind+1):
        a = a + str_[i]
     return a
  def split_b(str_, ind):
    b = ""
    for j in range(ind+1, len(str_)):
        b = b + str_[j]
    return b
  t = int(input())
for test_case in range(t):
    n = int(input())
    str_list = []
    str_dict = dict()
    for i in range(n):
        str_ = input()
        str_list.append(str_)
        if str_ in str_dict:
            str_dict[str_] += 1
        else:
            str_dict[str_] = 1
    out_str = []
    for i in range(n):
        out_str.append(0)
    i = 0
    for str_ in str_list:
        ok = 0
        for j in range(len(str_)):
            a = split_a(str_, j)
            if a in str_dict:
                b = split_b(str_, j)
                if b in str_dict:
                    ok = 1
                    out_str[i] = 1
        i += 1
    out  = ""
    for i in out_str:
        out += str(i)
    print(out)
  