def palindrome_cnt(str_list):
    count = 0
    for time in str_list:
        # print(time)
        if time[0] == time[4] and time[1] == time[3]:
            count += 1
    return count
  def convert_to_hhmm(number):
    hr = number // 60
    if hr < 10:
        hr = "0" + str(hr)
    mm = number - (int(hr) * 60)
    if mm < 10:
        mm = "0" + str(mm)
    return str(hr) + ":" + str(mm)
  t = int(input())
for test_case in range(t):
    time_str, x = map(str, input().split())
    x = int(x)
    seen_list = []
    given_hr = time_str[0] + time_str[1]
    given_mint = time_str[3] + time_str[4]
    given_time_str_num = int(given_hr) * 60 + int(given_mint)
    seen_list.append(time_str)
    matched = 0
    changed_time_num = given_time_str_num
    while not matched:
        changed_time_num += x
        if changed_time_num >= 1440:
            changed_time_num -= 1440
        time_cnv = convert_to_hhmm(changed_time_num)
        if time_cnv in seen_list:
            matched = 1
            # seen_list.append(time_cnv)
            break
        seen_list.append(time_cnv)
    # print(seen_list)
    print(palindrome_cnt(seen_list))
   