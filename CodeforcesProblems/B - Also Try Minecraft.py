n, m = map(int, input().split())
int_list = list(map(int, input().split()))
damage_list_from_start = [0]
damage_in_step_from_start = 0
damage_list_from_end = [0]
damage_in_step_from_end = 0
for i in range(n-1):
    if int_list[i+1] < int_list[i]:
        damage_in_step_from_start = damage_in_step_from_start + int_list[i] - int_list[i+1]
        # print(damage_in_step_from_start)
    damage_list_from_start.append(damage_in_step_from_start)
 # print(damage_list_from_start[t-1] - damage_list_from_start[s-1])
 for i in range(n-1):
    if int_list[i+1] > int_list[i]:
        damage_in_step_from_end = damage_in_step_from_end + int_list[i+1] - int_list[i]
        # print(damage_in_step_from_start)
    damage_list_from_end.append(damage_in_step_from_end)
 # print(damage_list_from_start)
# print(damage_list_from_end)
 for testcase in range(m):
    s, t = map(int, input().split())
    damage = 0
    if s < t:
        print(damage_list_from_start[t-1] - damage_list_from_start[s-1])
    else:
        print(damage_list_from_end[s-1] - damage_list_from_end[t-1])