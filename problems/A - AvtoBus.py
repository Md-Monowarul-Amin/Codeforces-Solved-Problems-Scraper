t = int(input())
for test_case in range(t):
    tyres = int(input())
    ans = -1
     if tyres % 2 == 0 and tyres >= 4:
        ans = 1
        if tyres % 4 == 0 and tyres % 6 == 0:
            minim = tyres // 6
            maxim = tyres // 4
        elif tyres % 4 == 0 and tyres % 6 != 0:
            maxim = tyres // 4
            if (tyres - 4) % 6 == 0:
                minim = (tyres - 4) // 6 + 1
            elif (tyres - 8) % 6 == 0:
                minim = (tyres-8) // 6 + 2
        elif tyres % 4 != 0 and tyres % 6 == 0:
            minim = tyres // 6
            maxim = (tyres - 6) // 4 + 1
        else:
            maxim = (tyres - 6) // 4 + 1
            if (tyres - 4) % 6 == 0:
                minim = (tyres - 4) // 6 + 1
            elif (tyres - 8) % 6 == 0:
                minim = (tyres - 8) // 6 + 2
            elif (tyres - 12) % 6 == 0:
                minim = (tyres - 12) // 6 + 3
        print(minim, maxim)
    else:
        print(-1)