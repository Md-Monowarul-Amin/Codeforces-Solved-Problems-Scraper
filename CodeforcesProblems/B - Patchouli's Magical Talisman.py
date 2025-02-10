def whether_power_2(integer):
    operation = 0
    while integer % 2 == 0:
        integer = integer / 2
        operation += 1
    return operation
  t = int(input())
for test_case in range(t):
    n = int(input())
    int_list = list(map(int, input().split()))
    number_of_even = 0
    for i in int_list:
        if i % 2 == 0:
            number_of_even += 1
    if number_of_even != n:
        print(number_of_even)
    else:
        minim = 10 ** 5
        ok = 1
        for i in int_list:
            out = whether_power_2(i)
            minim = min(minim, out)
        print(minim + n - 1)
   