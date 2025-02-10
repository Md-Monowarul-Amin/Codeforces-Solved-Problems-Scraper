t = int(input())
for test_case in range(t):
    a, b = map(str, input().split())
    a_count = 50
    opp_a = 1
    b_count = 50
    opp_b = 1
    if a[-1] == "S":
        a_count -= 1
        opp_a = -1
    elif a[-1] == "L":
        a_count += 1
        opp_a = 1
    else:
        opp_a = 0
     if b[-1] == "S":
        b_count -= 1
        opp_b = -1
    elif b[-1] == "L":
        b_count += 1
        opp_b = 1
    else:
        opp_b = 0
     for i in range(len(a)-1):
        a_count += opp_a
     for i in range(len(b)-1):
        b_count += opp_b
     if a_count > b_count:
        print(">")
    elif a_count < b_count:
        print("<")
    else:
        print("=")
  